# abstraction means hiding the personal details and displayed only essential information to the outside world or user
# class Car:
#   def __init__(self):
#     self.acc = False
#     self.brk = False
#     self.clutch = False

#   def start(self):
#     self.clutch = True
#     self.acc = True
#     print("car started....")

# car1 = Car()
# car1.start()

# practise question
class Account:
  def __init__(self,balance,accountNo):
    self.balance = balance
    self.accountNo = accountNo

  # debit method
  def debit(self,amount):
    self.balance -= amount
    print("Rs.",amount,"was debited")
    print("total balance = ",self.balance)


  def credit(self,amount):
    self.balance += amount
    print("Rs.",amount,"was credited")
    print("total balance = ",self.balance)

  def get_balance(self):
    return self.balance


account1 = Account(10000,12345)
print(account1.balance)
print(account1.accountNo)
account1.credit(1500)
account1.debit(500)


