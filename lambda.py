# lambda arguments: expression
#typically used when a simple funtion is needed that is used only once in the code, or it is used as an argument to higher order functions (functions that take other functions as argumets)
add10 = lambda x: x + 10 #creates a function that takes an argument x and evaluates and returns the expression x+10
print(add10(5))

def add10_func(x): #exactly the same as the above but longer
    return x + 10

mult = lambda x,y: x*y
print(mult(5,6))

#example
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
point2D_sorted = sorted(points2D)
print(point2D_sorted) #sorts the list by first argument (which is x coordinate)
point2D_sorted = sorted(points2D, key=lambda x:x[1]) #sorts by second argument
print(point2D_sorted)
point2D_sorted = sorted(points2D, key=lambda x:x[0]+x[1]) #sorts by sums of tuple
print(point2D_sorted)

# map(func, seq)
#map function transforms each element with a function
a = [1, 2, 3, 4, 5]
b = map(lambda x:x*2, a) #creates an pbject that needs to be converted to a list
print(list(b))
c = [x*2 for x in a] #same as above and faster

# filter(func, seq)
#filter func returns true or false and returns all elements that are evalauted at truea = [1, 2, 3, 4, 5]
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x:x%2 == 0, a) 
print(list(b))
c = [x for x in a if x%2==0] #same as above and faster

# reduce(func, seq)
#repeatedly applies function to elements and returns a single value
from functools import reduce
a = [1, 2, 3, 4, 5, 6]
prod = reduce(lambda x,y:x*y, a) #functions for reduce always have 2 arguments
print(prod)