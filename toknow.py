# Important
# if a list contain another list inside and to go through each element of the lists with for loop see the example below
mylist = [["sanjay", 24, 1997],["kulu", 22, 1999], ["balu", 24, 1998]]

for name, age, year in mylist:
    print(name,"age is: ", (age)," year born in ",year)