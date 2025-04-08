class Car:
  def __init__(self,type):
    self.type = type
  @staticmethod
  def start():
    print("car started...")
  
  @staticmethod
  def stop():
    print("car stops...")

class Mahindra(Car):
  def __init__(self,name,color):
    super().__init__(type)
    self.name = name
    self.color = color

car1 = Mahindra("petrol""Thar Roxx","black")
print(car1.name)
print(car1.color)
print(car1.start())
print(car1.stop())
print(car1.type)