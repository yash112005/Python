# def show(n):
#   if(n==0):
#     return
#    print(n)
#   show(n-1)

# show(5) 

# def fact(n):
#   if(n==0 or n ==1):
#     return 1
#   else:
#     return n*fact(n-1)  

# print(fact(6)) 


# def cal_sum(n):
#   if(n==0 ):
#     return 1
#   return cal_sum(n-1) + n

# sum = cal_sum(5)
# print(sum)


def print_list(list,idx):
  if(idx == len(list)):
    return
  print(list[idx])
  print_list(list,idx+1)

cities = ["delhi","pune","mumbai","lucknow","jabalpur"]
print_list(cities,0)

  
