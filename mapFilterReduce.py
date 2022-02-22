# from re import A
# from numpy import number


# numbers = ['3','34','45','44','56','66']

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
    
# numbers[2] = numbers[2] + 1
# print(numbers[2])

# # how the above problem can be solved using the map functions

# numbers = list(map(int, numbers))

# def sq(a):
#     return a*a

# num = [2,3,4,5,6,7,8,76,5,4]

# square = list(map(lambda x: x*x, num))
# print(square)

# def cube(a):
#     return a*a*a

# func = [sq, cube]
# for i in range(5):
#     val = list(map(lambda x:x(i),func))
#     print(val)


# Filter function 
list_1  =  [1,2,3,4,5,6,7]

def is_greater(num):
    return num>5


gr_than_5 = list(filter(is_greater,list_1))
print(gr_than_5)


# Reduce

from functools import reduce

list1 = [1,2,3,4]

num = reduce(lambda x,y:x+y, list1)

print(num)