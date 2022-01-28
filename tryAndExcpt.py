# check a program before you run it
num1 = input()
num2 = input()
try:
    print ("the sum of numbers ", int(num1)+int(num2))
    
except Exception as e:
    print(e)
    
print("Line is printed after the error")
    