# _ _init_ _ function is constructor in python
# creating class
class Student:
  # default contructor
  def __init__(self):
    pass
  #parametrised constructor
  def __init__(self,fullname):
    self.name = fullname

# creating object
s1 = Student("karan")
print(s1.name)

# self parameter is a reference to the current instance of the class and is used to access variables at belong to the class.
# class attribute class.attr is form when same thing is common for all object
# obj attribute give higher prefernce in comparison to class attributes

# methods
def hello(self):
  print("hello",self.name)

s1.hello() # to use methods