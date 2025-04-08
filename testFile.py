# opening a file
# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))

# writing a file
# f = open("demo.txt","w")
# f.write("I am hello")
# f.close()

f = open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()