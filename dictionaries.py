#Dictionaries: Key-Value pairs, Unordered, Mutable

#keys can also be number and tuples (they must be immutable, so no lists)
mydict = {"name": "Max", "age": 28, "city": "New York"}
# can also use dict function
mydict2 = dict(name="Ahmed", age=27, city="Alex")
#using tuples as keys
mytuple = (8,7)
mydict3 = {mytuple:15}

#obtaining values
value = mydict["age"]
print(value)

#adding extra pairs
mydict["email"] = "max@xyz.com"
mydict["email"] = "coolmax@xyz.com" #overwrites the previous value

#deleting pairs
del mydict["age"]
mydict.pop("city")
mydict.popitem() #removes last inserted item

#key if key is inside dict
if "name" in mydict:
    print(mydict["name"])
#another method for checking
try:
    print(mydict["name"])
except:
    print("Error")

# looping in dicts
for key, value in mydict.items():
    print(key)
    print(value)

#copying dicts
mydictcopy = mydict  #modifiying the copy modifies the original as well
mydictcopy = mydict.copy #creates actual copy
mydictcopy = dict(mydict) #creates acual copy

#merging 2 dicts
mydict = {"name": "Max", "age": 28, "email": "max@gmail.com"}
mydict2 = dict(name="Ahmed", age=27, city="Alex")
mydict.update(mydict2)
print(mydict)