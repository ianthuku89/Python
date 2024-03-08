#Returning multiple values from a function
def myfun():
  return 1,2,3

a,b,c = myfun()
print(myfun())
#Anonymous functions with lambda
x = 10
a = lambda y, x=x: x+y
print(a(10))
x = 20
b = lambda y, x=x: x + y
print(b(30))
#Example
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
     print(f(0))

