#Unpacking a sequence into separate variables
data = ['ACME',50,91.1,(2012,12,21)]
name,shares,price,date = data
print(name)
print(shares)
print(price)
print(date)

#Use of the star expression to unpack elements from iterables of varying length
records = [
 ('foo', 1, 2),
 ('bar', 'hello'),
 ('foo', 3, 4),
]
def do_foo(x, y):
 print('foo', x, y)
def do_bar(s):
 print('bar', s)
for tag, *args in records:
 if tag == 'foo':
    do_foo(*args)
 elif tag == 'bar':
      do_bar(*args)