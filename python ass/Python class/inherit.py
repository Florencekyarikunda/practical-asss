# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname=firstname
#         self.lastname=lastname

#     def printname(self):
#         print(self.firstname,self.lastname)

#         x=Person("Florence","Arinda")
#         printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()