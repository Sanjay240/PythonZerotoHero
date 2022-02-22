## F-String and abString
# string formating means you can insert varibles in between the string
me = "Sanjay"
a1 = 3

# a ="this is %s %s"%(me,a1)

import math

a = f"this is {me} {math.cos(45)}"

print(a)

# f string simply concat the string and the variabels in one sentence
