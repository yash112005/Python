# function used to perform specific tasks
# def func_name(para1,para2):
# func_name(arg1,arg2) to call function
#  some work
# return val

# def sum(a,b):
#   s = a + b
#   return s

# print(sum(2,6))  

# def cal_avg(a,b,c):
#   sum = a + b + c
#   avg = sum/3
#   print(avg)
#   return avg

# cal_avg(1,3,6) 

def calculator(usd_val):
  inr_val = usd_val *87.3
  print(usd_val,"USD = ",inr_val,"INR")

calculator(11) 