import requests as rq
from bs4 import BeautifulSoup
import json
from tqdm import tqdm

# 域名
domain = "http://njdxydjd.mh.libsou.com/"

"""
获得书籍URL列表
:returns: 书籍URL列表
"""


def getBookUrlList():
    bookUrlList = []
    # 26-37
    print("正在获取书籍URL列表")
    for cid in tqdm(range(26, 38)):
        index = rq.get(domain + "newbook?cid=" + str(cid))
        bookListDiv = BeautifulSoup(index.text, 'lxml').find("div", "bookList")
        bookHrefTag = bookListDiv.findAll("a")
        for book in bookHrefTag:
            bookUrlList.append(book.attrs['href'])
    return bookUrlList


"""
获得书籍信息
:param url 书籍URL
:returns: 书籍信息 字典格式
"""


def getBookInfo(url):
    tempUrl = domain + url
    book = {}
    bookPage = rq.get(tempUrl)
    # print(bookPage.text)
    book["type"] = BeautifulSoup(bookPage.text, 'lxml').find("p", "tit").get_text().replace("首页-经典阅读-", "").replace("[","").replace("]", "")
    bookInfo = BeautifulSoup(bookPage.text, 'lxml').find("div", "book_show_intro")
    book["name"] = bookInfo.find("dt", "font_blue").get_text().strip()
    for dd in BeautifulSoup(bookPage.text, 'lxml').findAll("dd"):
        ddText = dd.get_text()
        if "作者：" in ddText:
            book['author'] = ddText.replace("作者：", "").replace("著", "").strip()
        elif "出版社：" in ddText:
            book['publisher'] = ddText.replace("出版社：", "").strip()
        elif "出版时间：" in ddText:
            book['publicationDate'] = ddText.replace("出版时间：", "").strip()
        elif "页数：" in ddText:
            try:
                book['pageNum'] = int(ddText.replace("页数：", "").replace("页", "").strip())
            except ValueError:
                book['pageNum'] = 0
        elif "ISBN：" in ddText:
            book['ISBN'] = ddText.replace("ISBN：", "").strip()
    book['description'] = BeautifulSoup(bookPage.text, 'lxml').find(id="content").get_text().strip("\n").strip(
        "\r").strip()
    return book


if __name__ == '__main__':
    # 获得书籍列表
    bookUrlList = getBookUrlList()
    # 遍历列表获得书籍信息
    print("\n正在爬取书籍信息\n")
    for url in tqdm(bookUrlList):
        bookInfo = getBookInfo(url)
        fileName=bookInfo['name'].replace("《","").replace("》","").replace("/","").strip()
        # 存json文件
        with open("./bookData/" + fileName + ".json", "w") as f:
            json.dump(bookInfo, f)
