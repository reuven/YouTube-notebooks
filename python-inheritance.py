import marimo

__generated_with = "0.23.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    class Person:
        def __init__(self, name):
            self.name = name

        def greet(self):
            return f'Hello, {self.name}!'

    p1 = Person('name1')        
    p2 = Person('name2')

    print(p1.name) # does p1 have an attribute name? Yes, its value is "name1"

    print(p1.greet()) # does p1 have an attribute greet? No! Does p1's class, Person, have greet? Yes!
    print(p2.greet())
    return (Person,)


@app.cell
def _(Person):
    # we want a class that's almost identical to Person -- Employee!
    # the only difference will be that every instance of Employee also has an employee_id

    class Employee(Person):  # Employee inherits from Person, Employee is-a Person
        def __init__(self, name, id_number):
            super().__init__(name)   # super populates the invocation of __init__ with self (the instance)
            self.id_number = id_number

        # def greet(self):
        #     return f'Hello, {self.name}!'

    e1 = Employee('emp1', 1)        
    e2 = Employee('emp2', 2)

    print(e1.name)    # does e1 have an attribute name? Yes, value is 'emp1'
    print(e1.greet()) # does e1 have an attribute greet? No. Does Employee have greet? No! We go to the parent, Person -- it has greet.
    print(e2.greet())
    return (Employee,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Things to remember

    - Methods are defined as class attributes. They are attributes on the class, not on the instance.
    - When we invoke a method via the instance, it only works thanks to the ICPO rule (instance, class, parent, object)
    """)
    return


@app.cell
def _(Person):
    # MRO -- method resolution order

    Person.__mro__
    return


@app.cell
def _(Employee):
    Employee.__mro__
    return


@app.cell
def _():
    # Multiple inheritance

    class A:
        def __init__(self, **kwargs):
            super().__init__(**kwargs) 
            print('In A.__init__!')      
            self.z = kwargs['z']

    class B:
        def __init__(self, **kwargs):
            super().__init__() 
            print('In B.__init__!')
            self.y = kwargs['y']

    class C(A, B):
        def __init__(self, x, **kwargs):
            super().__init__(**kwargs)  # pass kwargs as keyword arguments
            print('In C.__init__')
            self.x = x

    c = C(10, y=20, z=30)
    return A, C


@app.cell
def _(C):
    C.__mro__
    return


@app.cell
def _(A):
    A.__mro__
    return


@app.class_definition
class MyClass:
    def show_super(self):
        s = super()
        print(f'{s.__self__=}')
        print(f'{(s.__self__ is self)=}')


@app.cell
def _():
    m = MyClass()
    return (m,)


@app.cell
def _(m):
    m.show_super() 
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
