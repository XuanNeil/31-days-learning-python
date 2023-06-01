'''
Python Lambda
- 1 lambda function is a small anonymous function.
- syntax: lambda arguments : expression
'''

# ví dụ:
x = lambda x: x + 10
print(x(5))

y = lambda x,y: x + y
print(y(10,25))

'''
Why use lambda function
- Để thực hiện 1 function anonymous bên trong 1 function khác.
'''
def myFn(n):
    return lambda a: a * n

myDoubler = myFn(2)
print(myDoubler(10))