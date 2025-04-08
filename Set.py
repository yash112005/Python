# set - set is collection of unordered items
# each element in the set must be unique and immutable
# in set key value are press nhi hota only values are stored
# its simply ignore the duplicate values
# set is mutable but element are immutable we can pass tuple but list and dict cant be

# collection = {1,2,3,4,5,"hello",5,5,2,2}
# print(collection)
# print(len(collection))

# empty set
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add((1,2,3,4,5))
# collection.remove(4)
print(collection)

# set method
# to add
collection.add(1)
# to remove
collection.remove(1)
# empties the set
collection.clear()
# remove random value
# collection.pop()
# combine both set value and return new
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10,1}
print(set1.union(set2))
# combine common value and return new\
print(set1.intersection(set2))



# collection = {"hello","hi","namaste","jai ho"}
# print(collection.pop())


