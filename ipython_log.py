# IPython log file


5+3
def myfunc(x, y):
    return f'{x=}, {y=}'
myfunc(10, 20)
# what if I want to pass any number of arguments?
# Python knows how many arguments I'm supposed to pass to a function -- if I pass too many, I'll get an error

myfunc(10, 20, 30)
# if I really insist on getting any number of arguments, then I'll need a parameter
# that can accept a variable number of arguments

# that is *args 

def myfunc(x, *args):
    return f'{x=}, {args=}'
myfunc()
myfunc(10)
myfunc(10, 20, 30, 40, 50)
def mydiv(x, y):
    print(f'{x=}, {y=}')
    return x / y
mydiv(10, 5)
# parameters: x   y
# argumentse: 10 5

mydiv(10, 5)  # positional arguments

# parameters: x  y
# arguments:  10  5

mydiv(x=10, y=5)  # now they're both keyword arguments!
# parameters: x  y
# arguments:  5  10

mydiv(y=10, x=5)  # now they're both keyword arguments!
def myfunc(**kwargs):   # kwargs will be a dict whose keys are the kwargs name, and values are kwarg values
    for key, value in kwargs.items():
        print(f'\t{key}:{value}')
myfunc(a=10, b=20, c=30)
myfunc(10, 20, 30)
def myfunc(x, *args, **kwargs):
    return f'{x=}, {args=}, {kwargs=}'
myfunc(10, 20, 30, 40, a=100, b=200, c=300)
