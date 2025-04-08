# list is a built-in data type that store set of a value
# it can store element of differnt types(int,float,string)

# string are immutable means which cannot change
# list are mutable means which can change
# marks = [45,89,23,74,85.1,96,"delhi"]

# print(marks[6])
# print(len(marks))
# marks[1]= " yash"
# print (marks)

# slicing in list
# print(marks[0:4])
# print(marks[:4])
# print(marks[4:])


# list method
list = [0,1,2,3,4,5,6]
#append
list.append(7)
print(list)
#sort
list.sort()
print(list)
#sort reverse
list.sort(reverse=True)
print(list)
#reverse
list.reverse()
print(list)
# insert
list.insert(0,"delhi")
print(list)
#remove
list.remove(0) # remove first occurance of element
print(list)
#pop
list.pop(3)
print(list) # remove element at index
