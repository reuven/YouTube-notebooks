import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    # most math operators in Python are *binary* operators
    # they have two arguments

    10 + 5
    return


@app.cell
def _():
    # I can also use variables
    x = 10
    y = 20

    x + y
    return (x,)


@app.cell
def _(x):
    # there is also a unary minus operator -- it reverses the sign of whatever is to its right
    -x
    return


@app.cell
def _(x):
    --x
    return


@app.cell
def _():
    n = 5
    n = +7   # let's assign the value 7 to n!

    n
    return


@app.cell
def _():
    # first part of their mistake was saying =+ and not += 
    # the += operator takes the value on the right, adds it to the value on the left, and assigns to the value on the left

    m = 5
    m += 7   # m = m + 7
    m
    return


@app.cell
def _():
    class MyClass:
        def __init__(self, x):
            self.x = x
        def __pos__(self):
            print(f'I am running unary +!')
            return self.x * 100


    my_object = MyClass(10)
    +my_object
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
