# dictonaries are used to store data value in key:value pairs
# they are unordered ,mutable(changeable)& dont allow duplicate keys

dict = {               # in key we dont use tuple list we only 
  "name" : "yash",    # use string ,int ,float
  "cgpa"  : 10,
  "marks"  : [98,99,100,95],
}
dict["name"] = "bharat" # assign new item or name
print(dict["name"])



# nested dictionaries
student = {
  "name"  : "yash",
  "subject" : {
    "chem"  : 98,
    "maths"  : 99,
    "phy"  : 99,
  }
}
# print(student["subject"])
# print(student["subject"]["chem"])


# dictionary methods
# return all the keys
print(list(student.keys()))

# return all values
print(list(student.values()))

#return all (key,val)pairs as tuples
pairs = (list(student.items()))
print(pairs[0])

# return the key according to value
print(list(student.get("name")))

# insert the specified item to the dictionary
student.update({"city" : "mumbai"})
print(student)