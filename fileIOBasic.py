# file Io basics 
# violitle - temporary memory RAM
# non volatile - permanent memory Hard disk
"""
read mode = open file for reading- default
write mode = open file for writitng
xclusive creation =  creates file if not exits
append =  add more content to a file
text mode =  text file have text data - default
binary mode = binary file
+ mode = open file for both reading and writing purpose
"""

# read(), readline(), readlines()- retrun results in list, 

f = open("sanjay.txt", "r")

for line in f:
    print(line)

content =  f.read()
print(content)

f.close()

# write for file deletes the existing valuses and write new line
# append mode to add to file keeping the data saved

f = open("sanjay.txt", "w")

f.write("This line is coming from the code\n")

f.close()

# Handle read and write both

f = open("sanjay.txt", "r+")
print(f.read())
f.write("without delelting")
f.close()

# to find the file pointer "f.tell()" tell pointer locations
# to change the pointer location  "f.seek()" reset the pointer location

# File with blocks it will closes the file automatically
with open("sanjay.txt") as f:
    a = f.read(4)
    print(a)