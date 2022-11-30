# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

#the counter stores the elements as dictionary keys and their counts as dictionary values
from collections import Counter
a = 'aaaabbbbbccccc'
mycounter = Counter(a)
print(mycounter)
print(mycounter.most_common(2)) #print the first two most common types (returns a list of tuples (2 dimensional))
print(list(mycounter.elements())) #returns a list of all elements

#namedtuple are easy to create and lightweight
from collections import namedtuple
Point = namedtuple('Point', 'x,y') #first arg is a string with the same name as the namedtuple (which is a class), second arg is a string with all the different fields seperated by a comma
pt = Point(1, -4)
print(pt)
print(pt.x)

#ordereddict is like a regular dict but remembers the orders (not as important in newer versions of python)
from collections import OrderedDict
ordereddict = OrderedDict()
ordereddict['a'] = 1
ordereddict['b'] = 2
ordereddict['c'] = 3
ordereddict['d'] = 4
print(ordereddict)

#same as normal dict but keys will have default values if they are not set yet
from collections import defaultdict
d = defaultdict(int) #default type of int
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c']) #will return default value of int which is zero

#deque is a double ended que that is used to add or remove elements from both ends. 
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3) #appends elements from the left side
print(d)
d.pop()
d.popleft() #removes element from left side
d.extend([4,5,6])
d.extendleft([9,8,8]) #extends elements from left side
print(d)
d.rotate(2) #rotates elements 2 places to the right
d.rotate(-1) #rotates elements 1 place to the left

