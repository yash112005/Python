# class method is bound to the class and receives the class as an implicit first argument
# note - static method cant access or modify state and generally for utility

class Person:
  name = "oyo"

  def changename(self,name):
    Person.name = name # class method or 
    # self.__class__.name = name (same)

     # another way
    # @classmethod
    # def changename(cls,name): 
    #   cls.name = name

p1 = Person()
p1.changename("gogo")
print(p1.name)
print(Person.name)