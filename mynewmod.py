# I only want to print when the mynewmod.py is being run as a standalone program
# when it is imported by another program, and used as a module, I want it to remain silent

if __name__ == '__main__':
    print(f'Hello from {__name__}!')

# x and y are global variables in mynewmod.py
x = 100
y = [10, 20, 30]

if __name__ == '__main__':
    print(f'Goodbye from {__name__}!')