import itertools
def count(n):
  while True:
    yield n
    n += 1

c = count(0)
for x in itertools.islice(c,10,20):
  print(x)

#Iterating over all possible permutations or combinations
items = ['a','b','c']
from itertools import permutations
for p in permutations(items):
  print(p)
#for permutations of smaller lengths
for y in permutations(items,2):
  print(y)
#producing a sequence of combinations of user input
from itertools import combinations
for z in combinations(items,3):
  print(z)
#2 combinations
  for z in combinations(items,2):
    print(z)
#1 combination
  for z in combinations(items,1):
    print(z,"\n")

#iterating over multiple sequences
xpts = [1,23,45,67,89]
ypts = [43,546,76,87]
for x,y in zip(xpts,ypts):
  print(x,y, "\n")

#iterating over multiple sequences simultaneously usin zip()
  from itertools import zip_longest
  for i in zip_longest(xpts,ypts):
    print(i,"\n")

#filling in empty values
for i in zip_longest(xpts,ypts, fillvalue = 0):
  print(i,"\n")

#iterating on items in separate containers
from itertools import chain
a = [1,2,3,4]
b = ['x','y','z']
for i in chain(a,b):
  print(i)


