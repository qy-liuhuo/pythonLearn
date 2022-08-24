from PIL import Image


class ImgEncode:

    def __init__(self, fileUrl, imgUrl):
        self.fileUrl = fileUrl
        self.imgUrl = imgUrl
        self.__readFile()
        self.__readImg()
        # 新建一个生成器
        self.pg=self.__generateXY()

    # 将二进制字符串补足到9bit(因为三个像素点能存9bit,注意是前面补0才能保证编码不变)
    def __nineBin(self, bin):
        bin = '0' * (9 - len(bin)) + bin
        return bin

    # 读文本文件
    def __readFile(self):
        with open(self.fileUrl, 'r') as f:
            string = f.readline()
        binaryStr = [format(ord(c), 'b') for c in string]
        binaryStr = list(map(self.__nineBin, binaryStr))
        print(binaryStr)
        self.binaryStr = binaryStr

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

    # 文本隐藏
    def encode(self):
        # 获得文本的二进制编码列表
        strLen = len(self.binaryStr)
        strLenBin = self.__nineBin(bin(strLen)[2:])  # 不需要开头的0b,补足到9位
        # 首先写入长度
        self.__writeToPix(strLenBin)
        for byte in self.binaryStr:
            self.__writeToPix(byte)
        self.img.save("encoded_"+self.imgUrl)

    # 修改像素点，一次写入9bit
    def __writeToPix(self, byte):
        for i in range(3):
            p = next(self.pg)
            pix = self.img.getpixel(p)
            newPix=[]
            for j in range(3):
                bit=int(byte[i * 3 + j])
                lastBit = pix[j]%2
                if lastBit < bit:
                    newPix.append(pix[j]+1)
                elif lastBit > bit:
                    newPix.append(pix[j]-1)
                else:
                    newPix.append(pix[j])
            self.img.putpixel(p,tuple(newPix))


if __name__ == '__main__':
    test = ImgEncode("text.txt", "img.png")
    test.encode()
