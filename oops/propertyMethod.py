# property @property decorator on any method in the class to use the method as a property
class Student:
  def __init__(self,phy,chem,math):
    self.phy = phy
    self.chem =  chem
    self.math = math
    self.percentage = str((self.phy+self.chem+self.math)/3)

    # def calPercenatge(self):
   #   self.percentage = str((self.phy+self.chem+self.math)/3)

  @property
  def percentage(self):
    return str((self.phy+self.chem+self.math)/3)

s1 = Student(99,97,98)
print(s1.percentage)
s1.phy = 100

print(s1.percentage)
