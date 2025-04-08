class Student:
  def __init__(self,name,accountNo,accpass):
    self.name = name
    self.accountNo = accountNo 
    self.__acc_pass =acc_pass # to make private use __ (underscore underscore in front of name)
    # method ko bhi private bana sakte hai same logic above
    def __hello(self):
      print("hello")
    
    def welcome(self):
      self.__hello

s1 = Student("karan",12345,"abcde")
# print(s1.name)
# print(s1.accountNo)
# print(s1.__acc_pass)
print(s1.__hello)
print(s1.welcome())



