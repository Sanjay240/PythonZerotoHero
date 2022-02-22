#Snake Water Gun

# use random choice function

import random;

choices = ['rock', 'paper','sciscor']

choice = random.choice(choices)
 
userInput = input("Enter your choice 'rock','paper','sciscor': ")

if(choice==userInput):
    print("draw")

elif(choice == 'rock' and userInput == 'paper'):
    print("you win")

else:
    print("need more functionality")



