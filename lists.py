grocery = ['harpic', 'vim bar','choclate', 'lists'];
print(grocery);

# list can have both the numbers and strings
# list indexing grocery[2]

## slicing

print(grocery[0:4]) # slicing of list returns a list

# extended slice
numbers = [1,2,3,4,5,6]

# negtive slicing should on be -1 recomeded [1:2:-1] reverse lists

numbers.append(7) # add at the last of list

numbers.insert(1,-1) # adds at a specific index
print(numbers)

numbers.remove(7) # removes the given value
numbers.pop()     # remove the last element

numbers[1] = 98
print(numbers)

# Mutable - can change i.e list
# Immutable - cannot change i.e tuple

# for only one element in tuple add comma at the last to make it tuple


# substitue of using the temp variable
a = 1
b = 4
a ,b = b,a
print(a,b)
