""" Write a Python program to find a specific string in the list using a simple 
for loop and if condition"""

list2 = ['anand','jeel','yash','om','sunny']
ch = "sunny"
for i in list2:
  if list2 == ch:
    ch+=1
print(ch,"Yes avalible")