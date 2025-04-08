# class Circle:
#   def __init__(self,radius):
#     self.radius = radius

#   def calcuArea(self):
#     return 3.1415*self.radius*self.radius

#   def perimeter(self):
#     return 2*3.1415*self.radius

# c1 = Circle(4)

# print(c1.calcuArea())
# print(c1.perimeter())


# class Employee:
#   def __init__(self,role,dept,salary):
#     self.role = role
#     self.dept = dept
#     self.salary = salary

#   def showDetails(self):
#     print("role : ",self.role)
#     print("dept : ",self.dept)
#     print("salary : ",self.salary)

# class Engineer(Employee):
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
#     super().__init__("engineer","IT","75000")

# e1 = Engineer("xyz",25)
# e1.showDetails()
# print(e1.name)


class Order:
  def __init__(self,items,price):
    self.items = items
    self.price = price

  def __gt__(self,odr2):
    return self.price > odr2.price

odr1 = Order("chips",25)
odr2 = Order("chai",30)
print(odr1 > odr2)

