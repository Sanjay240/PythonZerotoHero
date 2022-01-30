# l = 10 # Global

# def function1(n):
#     m = 5 #local
#     global l 
#     l = l+15
#     print(m,l, "Local variavle printed")
    
# function1(3)

# ## Recursion and Recursive Method

# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)

# factorial_recursive(5)

# ## 0,1,1,2,3,5,8,13,21 use recursive method to print it fibonacci series

# def special_series(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return special_series(n-1)+special_series(n-2)

# print("Fibonacchi series begans")
# print(special_series(5))
        
    
# ## Lambda functions and Anonymous functions
# print("Lambda functions")

# minus = lambda x,y: x-y

# print(minus(9,4))

# def a_first(a):
#     return a[1]

# a = [[1,14], [5,6],[8,23]]

# a.sort(key=lambda a:a[1])

# print(a)

# ## Modules in python 

import random

random_number = random.randint(0,5) # 0,5 inclusive

rand = random.random() *100 #b/w 0 to 100

lst = ["Star Plus", "DD1","Aaj Tak","Channel"]

choice = random.choice(lst) # choose random element from choices