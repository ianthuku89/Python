#Swap first and last elements of a list
def swaplist(new_list):
  new_list[0],new_list[-1] = new_list[-1],new_list[0]
  return new_list

new_list = [1,2,3,4,5,6,7]
print(swaplist(new_list))
#getting length of a list in python
m = len(new_list)
print(m)
#Check if element exists in list
i = 32
if  i in new_list:
    print("Exists")
else:
    print("Does not exist")
#Reversing a list
def reverse(new_list):
   new_list= new_list[::-1]
   return new_list

print(reverse(new_list))
#reversing using reversed function
new_list = [1,2,3,4,5,6,7]
new_list.reverse()
print("Using reverse()", new_list)
print("Using reversed()", new_list(reversed(new_list)))

