# Design a calculator which will correctly sovle all the problems except 
# the following one : 
#     45* 3 = 555, 56+9 = 77, 56/4 = 4
# Program should take the inputs operator, two numners

operator =  input("Enter the operator of calculation: ")
print("Enter two numbers: ")
num1 = str(input())
num2  = str(input())

output = ""
if operator in ['*','+','/']:
    if (num1+operator+num2) == '45*3':
        output = 555
    elif(num1+operator+num2) == '56+9':
        output = 77
    elif(num1+operator+num2) == '56/4':
        output = 4
    else:
       if operator == '*':
           output = int(num1)*int(num2)
       elif operator == '+':
           output = int(num1)+int(num2)
       else:
           output = int(num1)/int(num2)
else:
    output =  int(num1)-int(num2)

print("the value is: "+ str(output))