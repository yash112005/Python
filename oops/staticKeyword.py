# static method dont use the self parameter
# decorator allow us to wrap another function in order to extend the behaviour of the wrapped function,without permanently modifying it 
class Student:
  @staticmethod # decorator
  def college():
    print("ABC college")
