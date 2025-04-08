# a = int (input("enter 1st number :  "))
# b = int (input("enter 2nd number :  "))
# print(a>=b)

# movie1 = input("enter name of 1st movie : ")
# movie2 = input("enter name of 2nd movie : ")
# movie3 = input("enter name of 3rd movie : ")
# list = [movie1,movie2,movie3]
# print(list)

# list1 = [1,2,3,1]
# list2  =[1,2,3,4,5,6]
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if(copy_list1 == list1):
#   print("palindrome ")
#   else:
#     print("not palindrome")


# grade = ["C","D","A","A","B","B","A"]
# grade.sort()
# print(grade)

# dict = {
#   "table" : ["a piece of furniture ","list of facts & figures"], # if one key and two values are present the we can store it in form of list and tupple
#   "cat" : "a small animal"
# }
# print(dict)


# subjects = {"python","java","c++","C","javascript","python","python","java","java","c++"}
# print(len(subjects))



# marks = {}
# x = int(input("enter phy : "))
# marks.update({"phy" : x})
# y = int(input("enter maths : "))
# marks.update({"maths" : y})
# z= int(input("enter chem: "))
# marks.update({"chem" : z})
# print(marks)

# values = {9,"9.0"} # in python 9 and 9.0 has same hash value th output is only 9 but to print both store one of them in string in a set

# print(values)
# 2nd solution of above
# values = {
#   ("float",9.0),
#   ("int",9)
# }
# print(values)

# loop question

# nums = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# for el in nums:
#   print(el)
#   i+=1


# n = 6
# sum = 0
# for i in range(n+1):
 
#   sum +=i

# print("sum : ",sum)  


# n = 5
# product = 1
# i = 1
# while i<=n:
#     product *=i
#     i+=1

# print("product is : ",product)


# n = 5
# product = 1
# i = 1
# for i in range(1,n+1):
#     product *=i
#     i+=1

# print("product is : ",product)


class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for val in self.'
        marks:
            sum += val
        print("hi",self.name,"your avg score is : ",sum/3)
        

s1 = Student("karan",[98,99,97])

s1.average()



