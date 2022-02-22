from pip import main
import sklearn

def printhar(string):
    return f"ye stirng muje dede {string}"

def add(num1,num2):
    return num1+num2+5


## __name_ will have the main value if run in same program
# and will have the class vlaue if run from another class

if __name__ == '__main__':
    print(printhar("sanjay"))
    o = add(4,6)
    print(o)