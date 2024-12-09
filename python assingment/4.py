""" Practical Example 4: Print this pattern using nested for loop: 
 
markdown 
Copy code 
* 
** 
*** 
**** 

"""

row =6
for i in range(1,row):
  for i in range(1,i+1):
    print('*',end=" ")
  print()
