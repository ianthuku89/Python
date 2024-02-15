#Creating new iteration patterns
def frange(start, stop, increment):
    x = start
    while x < stop:
      yield x
      x += increment
 #Iterate over the function using a for loop
for n in frange(0, 4, 0.5):
      print(n)