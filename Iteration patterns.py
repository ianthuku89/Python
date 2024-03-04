#Creating new iteration patterns
def frange(start, stop, increment):
    x = start
    while x < stop:
      yield x
      x += increment
 #Iterate over the function using a for loop
for n in frange(0, 4, 0.5):
      print(n)
#iterating in reverse
a=[1,2,3,4,5,6]
for x in reversed(a):
    print(x)
#using the _Reversed()_ function
class Countdown:
    def __init__(self,start):
        self.start= start
#forward iterator
    def _iter_ (self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
#reverse iterator
    def _reversed_ (self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
