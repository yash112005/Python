# operator and dunder function
# a + b        a.__add__(b)
# a - b        a.__sub__(b)
# a / b        a.__truediv__(b)
# a * b        a.__mul__(b)
# a % b        a.__mod__(b)

class Complex:
  def __init__(self,real,img):
    self.real = real
    self.img = img

  def showNumber(self):
    print(self.real,"i +",self.img,"j")

  def __add__(self,num2): # dunder function
    newReal = self.real + num2.real
    newImg = self.img + num2.img
    return Complex(newReal,newImg)

num1 = Complex(1,3)
num1.showNumber()
num2 = Complex(5,2)
num2.showNumber()
num3 = num1 + num2  # operator overloading
num3.showNumber()