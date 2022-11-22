# Strings: ordered, immutable, text representation

#single or double quotes are the same
mystring = """Hello  
world""" 
char = mystring[-1]
# mystring[1] = 'h' #doesnt work as they are immutable
print(mystring)
print(char)

#slicing works as lists, using -1 in the step reverses the order

#concatinating
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name

#iterating
for i in greeting:
    print(i)

#check if substring is in string
if "Hell" in greeting:
    print("yes")
else:
    print("no")

#removing extra white space at beg and end
mystring = "            Hello           "
mystring = mystring.strip()
print(mystring)

#covert to upper and lower cases
mystring = mystring.upper()
mystring = mystring.lower()

#check if string starts or ends with certain subset
print(mystring.startswith("He"))
print(mystring.endswith('o'))

#finding index of substring
print(mystring.find('el')) #returns -1 if no substring found

#finding number of characters
print(mystring.count('l'))

#replacing
print(mystring.replace('hello', 'Hi'))

#convert string into list of words and vise versa
mystring = 'how, are you, doing'
mylist = mystring.split(',') #default arg is space
print(mylist)
mystring = '!'.join(mylist) #will put ! between each element
print(mystring)


#since a string is immutable, adding strings with +,  or += always 
#creates a new string, and therefore is expensive for multiple operations
from timeit import default_timer as timer
my_list = ["a"] * 1000000
#bad
start = timer()
a = ""
for i in my_list:
    a += i
end = timer()
print("concatenate string with + : %.5f" % (end - start))

#good
start = timer()
a = "".join(my_list)
end = timer()
print("concatenate string with join(): %.5f" % (end - start))

#formating using newer f-strings method
var = "Tom"
var2 = 3.234234
mystring = f'the variables is {var} and {var2*3.5}'
print(mystring)
