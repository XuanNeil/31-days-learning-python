'''
Python Functions
'''

# 1. Creating a function
def myFunction():
    print("This is a function")

myFunction()

# 2. Arguments
def myName(fname):
    print('Name: ' +fname)

myName("Neil")

# 3. *args
def myKid(*args):
    print(args[0])

myKid("Neil", "Ha", "No")

# 4. Argument keyword tùy ý, **kwargs
def fnKid(**kid):
    print('Name: ' + kid['fname'] + kid["lname"])
fnKid(fname = "Ha", lname = 'Neil')

# 5. Return value -> use the return statement.

# 6. The pass statement
def myFn():
    pass

