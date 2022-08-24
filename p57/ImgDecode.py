from PIL import Image


class ImgDecode:

    def __init__(self, imgUrl, fileUrl):
        self.fileUrl = fileUrl
        self.imgUrl = imgUrl
        self.__readImg()
        # 新建一个生成器
        self.pg = self.__generateXY()
        self.decode()
        self.__writeFile()
    # 将二进制字符串补足到9bit(因为三个像素点能存9bit)
    def __nineBin(self, bin):
        bin = bin + '0' * (9 - len(bin))
        return bin

    # 写文本文件
    def __writeFile(self):
        with open("decoded_"+self.fileUrl,"w") as f:
            f.write(self.resultStr)
    # 读图片对象
    def __readImg(self):
        self.img = Image.open(self.imgUrl)
        self.imgWidth, self.imgHight = self.img.size

    # 生成器函数，用于逐个生成x,y坐标
    def __generateXY(self):
        nowPix = 0
        while nowPix < self.imgWidth * self.imgHight:
            yield (nowPix % self.imgWidth), (nowPix // self.imgWidth)
            nowPix += 1
    def binToInt(self,byte):
        num=0
        for i in range(len(byte)):
            num*=2
            num+=int(byte[i])
        return num

    # 文本隐藏
    def decode(self):
        # 首先获得长度
        l=self.binToInt(self.__getByteFromPix())
        byteList=[]

        for i in range(l):
            byteList.append(self.__getByteFromPix())
        self.byteList=[chr(int(i,2)) for i in byteList]
        self.resultStr="".join(self.byteList)

    # 修改像素点，一次写入9bit
    def __getByteFromPix(self):
        byte = ""
        for i in range(3):
            p = next(self.pg)
            pix = self.img.getpixel(p)
            for j in range(3):
                byte += str(pix[j] % 2)
        return byte


if __name__ == '__main__':
    test = ImgDecode("encoded_img.png", "decodeFiles.txt")