#tuples cant be changed
# tuples are ordered, ummutable, allow duplicate elements

mytuple = ("Max", 28, "Boston")

# to create a tuple with a single element
mytuple = ("Max",) #dont forget the comma at the end or it will be a string

#elements will be accessed via square brackets
item = mytuple[0]

# can iterate over items
for x in mytuple:
    print(x)

#check if element is in tuple
if "Max" in mytuple:
    print("yes")
else:
    print("no")

#count elements inside tuple
mytuple = (1,2,3, "x", "y")
number = mytuple.count('x') #checks how many x are in mytuple
index = mytuple.index(2) #returns first occurance of 2

#convert tuple into list
mylist = list(mytuple)
mytuple2 = tuple(mylist)

#slicing, last index is not included
a = (1,2,3,4,5,6,7)
b = a[1:5:2]

#unpacking
mytuple = ("max", 28, "Boston")
name, age, city = mytuple #number of elements must match number of variables
print(name)
print(age)
print(city)

mytuple = (1,2,3,4,5)
i1, *i2, i3 = mytuple
print(i1)
print(i2)
print(i3)

#list is always larger than tuple
import sys
import timeit
mylist = [1,2,3, "hello"]
mytuple = (1,2,3, "hello")
print(sys.getsizeof(mylist),bytes) #obtains the size of the list
print(sys.getsizeof(mytuple), bytes) #optains the size of the tuple
print(timeit.timeit(stmt="[1,2,3,4,5]",number=1000000)) #takes much longer to create 1 million lists than tuples
print(timeit.timeit(stmt="(1,2,3,4,5)",number=1000000))



