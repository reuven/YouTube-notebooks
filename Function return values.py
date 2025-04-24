

import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    some_numbers = [10, 15, 17, 19, 24, 53, 92]

    # I want to calculate the mean of these numbers
    numbers_total = sum(some_numbers)
    return numbers_total, some_numbers


@app.cell
def _(numbers_total, some_numbers):
    # Now, let's really get the mean

    numbers_mean = numbers_total / len(some_numbers)  
    return (numbers_mean,)


@app.cell
def _(numbers_mean):
    print(numbers_mean)
    return


@app.function
def mean(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average


@app.cell
def _(some_numbers):
    x = mean(some_numbers)
    print(x)
    return


@app.cell
def _():
    mean([10, 20, 30])
    return


@app.cell
def _(some_numbers):
    print(mean(some_numbers))
    return


@app.cell
def _(some_numbers):
    # REPL -- read, eval, print loop
    # in a notebook, if the final line of the cell is an expression (i.e., gives a value back), then we see that value

    some_numbers[0]
    return


@app.cell
def _():
    10 + 10
    20 + 20 
    30 + 30
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
