
# 文章写入文件
str="Dreaming is the easy part. Acting on the dream is harder. Recognize that a dream is a journey. On the simplest level, it takes commitment, time, desire, and courage. But rarely is something great easily realized. Dreaming is recognizing and embracing the potential for greatness and seeking it in all areas of your life. Believe in your dreams and your ability to accomplish them. Keep your dreams in front of you. I'm here to challange you to reach for your dream. Do not be afraid to dream. Never forget, if you can dream it, you can do it!"
with open("test.txt","w") as f:
    f.write(str)
with open("test.txt","r") as f:
    lines=f.readlines()
    str=""
    for line in lines:
        str+=line

# 删除标点符号
str=str.replace(".","").replace(",","").replace("!","")
# 删除空格
wordList=str.split(" ")

# 防止把空格算进来
if " " in wordList:
    wordList.remove(" ")

wordSet=set(wordList)

print("单词数目：%d" % len(wordSet))

for i in range(10):
    print(wordSet.pop())