# Functions that return an object that can be iterated over
#they generate the items inside the object lazily, they generate items one at a time and only when asked for it

def mygenerator():
    yield 3
    yield 2
    yield 1

#creating an iterable object g
g = mygenerator()
#looping over the elements
for i in g:
    print(i)

#another method
f = mygenerator()
value = next(f)
print(value)
value = next(f)
print(value)

#generators can be used as inputs to functions that take iterables
z = mygenerator()
print(sorted(z))
print(sum(z))

#another example
def countdown(num):
    print('starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
#runs until the first yield statement then stops
value = next(cd)
print(value)
#runs once again until next yield statement
print(next(cd))

#generators are very memory efficient
import sys #to analyze the size of the objects
def firstn(n): #function that returns sequence from 0 to n
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(firstn(1500000)))
print(sys.getsizeof(firstn_generator(150000)))

# fibonacci sequence example
def fibonacci(limit):
    # 0 1 2 3 5 8 13 21
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

#generator expressions
mygenerator = (i for i in range (10) if i%2==0) #obtains all even elements from 0 to 9
for i in mygenerator:
    print(i)

mylist = [i for i in range(10) if i%2==0] #same as above but generates list
