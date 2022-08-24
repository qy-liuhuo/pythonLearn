class People:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def moveto(self, newCity):
        self.city = newCity

    def __str__(self):
        return str(self.name)+ ","+str(self.city)

    def __lt__(self, other):
        return self.city < other.city



if __name__ == '__main__':
    peoples=[People("a","beijing"),People("b","nanjing"),People("c","shanghai"),People("d","baoding"),People("e","tangshan")]
    peoples.sort()
    for i in peoples:
        print(i)