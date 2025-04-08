import random

target = random.randint(1,100)

while True:
  userchoice = input("Guess the target or Quit(Q) : ")
  if(userchoice == 'Q'):
    break
  userchoice = int(userchoice)
  if(userchoice == target):
    print("You Correct Guess the Number!!")
    break
  elif(userchoice < target):
    print("your number was too small.Guess Bigger...")
  else:
    print("your number was too large.Guess Smaller...")

print("----GAME OVER----")