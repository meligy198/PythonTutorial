import random

from scipy import rand #generates pseudo random numbers
random.seed(1) #optional, makes it reproducable 
a = random.random() #random float from 0 to 1
b = random.uniform(1, 10) #random float within given range
c = random.randint(1, 10) #random integer from 1 to 10
d = random.normalvariate(0, 1) #normal distribution, mean 0, std 1
mylist = list("ABDEFGH")
e = random.choice(mylist) #pick a random element from the list
f = random.sample(mylist, 4) #pick 4 unique elements from the list
g = random.choices(mylist, k=3) #picks 3 elements from list (can be duplicates)
h = random.shuffle(mylist) #shuffles list

#because above numbers are reproducable, use the secrets module (slower)
import secrets
i = secrets.randbelow(10) #rand int from 0 to 9
j = secrets.randbits(4) #generates a random number of 0 to 2^4
k = secrets.choice(mylist) #picks a random element

#numpy random arrays
import numpy as np
np.random.seed(1) #optional
l = np.random.rand(3,2) #rand arr of size 3x2
m = np.random.randint(3, 10, (5,3)) #rand arr from 0 to 9 and size 5x3
n = np.random.shuffle(m) #shuffles array m


