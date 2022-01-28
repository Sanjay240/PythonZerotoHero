# creat a dictionary and take input from the user and return the meaning of the word form the dictionary

myDictionary = {"sanjay":"my name","leader": "Inspire/Motivate","py": "python", "code":"computer language" }

print("Enter a number key from dictionary:")
keyEntered = input()

value = myDictionary[keyEntered]
print("Value of the word is: "+ value)