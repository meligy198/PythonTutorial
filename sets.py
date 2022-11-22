# Sets: unordered, mutable, no duplicates

myset= {1, 2, 3, 4} #duplicates are ignored
#myset = {[1,2,3,4,4,4,4]}
myset = {"hello"} #ignores extra set
myset = set() #empty set

# adding elements
myset.add(2)
myset.add(3)

#removing elements
myset.remove(3) #will create error if element removed is not in set
myset.discard(4) #will not create an error

#iterating
for i in myset:
    print(i)

#checking for elements
if 2 in myset:
    print("yes")

#union, intersetion and difference 
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}
u = odds.union(evens) #combines elements from 2 sets
i = odds.intersection(primes) #obtains elements common in both sets
d = odds.difference(primes) #returns a set with all elements in the first set that are not in the second set
s = odds.symmetric_difference(primes) #returns a set with all the uncommon elements from both sets

#modifying sets, can also use above 3 methods with _update at the suffix
myset.update(odds) #concatination without duplication
myset.intersection_update(odds)

#subsets
print(myset.issubset(odds)) #returns boolean
print(myset.issuperset(odds)) #returns boolean, opposite of above
print(myset.isdisjoint(odds)) #returns boolean, no common elements

#copying
myset2 = myset #modifying copy modifies original
myset2= myset.copy()
myset2 = set(myset)

#clearing a set
myset.clear()

#frozen sets: immutable version of set, cannot use normal set methods
myset = frozenset([1,2,3,4,5])


