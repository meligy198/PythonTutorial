# lists: ordered, mutable, allows for duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

# lists can contain different data types
mylist2 = list()
mylist2.append(5,True, "apple", "apple")

# access items with index (starts at 0) (-1 is the last item)
item = mylist2[0]
print(item)

# iterate over elements in lists
for i in mylist2:
    print(i)

# check if item is in list
if "banana" in mylist:
    print("yes")
else:
    print("no")

#check length
print(len(mylist))

# insert item at specific position
mylist.insert(1, "blueberry")

#remove items
mylist.remove("cherry")
mylist.pop() #removes last item
mylist2.clear() # empty list

#reverse list
mylist.reverse()

#sorting
mylist = [2,1,2,3,2]
mylist.sort() #overwrites existing list

newlist = sorted(mylist) #creates new list

#create a list of duplicate elements
mylist = [0]*5

#concate lists
mylist3 = mylist + mylist2

# create a list between x+1 and y in steps of z
x = 1
y = 5
z = 1
a = mylist[x:y:z]

#copying lists
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
list_cpy.append("lemon") #modifies both lists
list_cpy2 = list_org.copy
list_cpy2 = list(list_org)
list_cpy2 = list_org[:]

#list comprehension
a = [1,2,3,4,5,6]
b = [i*i for i in mylist] #creates new list of squared elements of a

