# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a,b) #computes the cartersian product, outputs object which has to be converted to list
print(list(prod))

from itertools import permutations #returns all possible orderings of an input
a = [1, 2, 3]
perm = permutations(a, 3) #3 is the length of the of permutation
print(list(perm))

from itertools import combinations, combinations_with_replacement #gives all possible combinations with a specified length
a = [1, 2, 3, 4]
comb = combinations(a, 2) #2 is the length of the combination
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

from itertools import accumulate #makes an iterator that returns accumulated sums or any other binary function given as input
import operator
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul) #will accumulate the product of the elements
print(list(acc))

from itertools import groupby #makes an iterator that returns keys and groups from an iterable, don't use it w 5alas
def smaller_than_3(x):
    return x<3
a = [1, 2, 3, 4]
grp_obj = groupby(a, key=smaller_than_3) #key is function
grp_obj = groupby(a, key=lambda x:x<3) #same as above
for key, value in grp_obj:
    print(key, list(value))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 35}, {'name': 'Lisa', 'age': 25}, {'name': 'Claire', 'age': 28}]
grp_obj = groupby(persons, key=lambda x:x['age'])
for key, value in grp_obj:
    print(key, list(value))

from itertools import count, cycle, repeat 
for i in count(10): #creates an infinite loop that starts at 10 and then adds one for ever repetition
    print(i)
    if i == 15:
        break
a = [1, 3, 4]
for i in cycle(a): # cycles infinitly through an iterable
    print(i)
for i in repeat(1, 5): #repeats 1 for 5 times
    print(i)
