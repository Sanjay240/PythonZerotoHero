def function_name_print(a,b,c,d):
    print(a,b,c,d)

function_name_print('Sanjay','kulu','blau','salu')

# adding more parameter to funtionality changing the param is not a 
#good way

def funargs(*args):
    for item in args:
        print(item)
    
har = ('Sanjay','kulu','blau','salu')

funargs(*har)

# kwargs kya hota h 
kw = {"Rohan":"Monitor", "Harry":"Fitness Trainer"}

def funargs(*args,  **kwargs):
    for item in args:
        print(item)
        
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
# def funargs