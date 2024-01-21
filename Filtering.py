#Use of a list comprehension
mylist=  [1,2,3,-5,-6,-7,-8,9,6,56]
result =[n for n in mylist if n> 0]
print(result)
#Use of a generator expression
pos = [n for n in mylist if n<0]
for x in pos:
  print(x)

#using the filter() function
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
 try:
    x = int(val)
    return True
 except ValueError:
   return False
ivals = list(filter(is_int, values))
print(ivals)
