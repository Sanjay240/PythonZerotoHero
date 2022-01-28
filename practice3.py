# Pattern printing
"""
take a input integer from user
boolen variable input
Sample output
true n =5
*
**
***
****
*****

false n = 5
*****
****
***
**
*
"""

num = int(input("Enter a ingeger input: "))
flag = int(input("Enter 0 or 1: "))
pic = ""
if flag == 0:
    pic = False
else: 
    pic = True
    
gate = 1
if pic:
    while (gate <= num ):
        print('*'*gate)
        gate += 1
else:
    while(num != 0):
        print('*'*num)
        num -= 1
    
    
    