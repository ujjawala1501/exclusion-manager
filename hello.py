class school():
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname  = lname

def demo(self):
    print(self.firstname,self.lastname)


class Student(school):
    pass


obj1 = Student("ujjawala","katakwar")

obj1.demo()
