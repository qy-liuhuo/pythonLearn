from MagusPythonLearn.p48.people import People


class Teacher(People):
    def __init__(self,name,city,school):
        super(Teacher,self).__init__(name,city)
        self.school=school

    def moveto(self, newSchool):
        self.school=newSchool

    def __lt__(self, other):
        return self.school < other.school


    def __str__(self):
        return str(self.name)+ ","+str(self.city)+","+self.school

if __name__ == '__main__':
    teachers=[Teacher("a","beijing","s1"),Teacher("b","nanjing","s2"),Teacher("c","shanghai","s3"),Teacher("d","baoding","s4"),Teacher("e","tangshan","s5")]
    teachers.sort()
    for i in teachers:
        print(i)