class MyList(list):
    def product(self):
        num=1
        for i in self:
            num*=i
        return num

if __name__ == '__main__':
    myList=MyList([1,2,3,4,5])
    print(myList.product())