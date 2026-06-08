import marimo

__generated_with = "0.23.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    x = 12345.678901
    type(x)
    return (x,)


@app.cell
def _(x):
    round(x)  # with one argument, I'll get back an integer
    return


@app.cell
def _():
    round(12345.1)
    return


@app.cell
def _():
    round(12345.9)
    return


@app.cell
def _():
    round(12345.5)
    return


@app.cell
def _(x):
    # 2nd argument to round -- how many digits to keep?
    round(x, 3)
    return


@app.cell
def _(x):
    round(x, 2)
    return


@app.cell
def _():
    round(3.5)
    return


@app.cell
def _():
    round(4.5)
    return


@app.cell
def _():
    round(5.5)
    return


@app.cell
def _():
    # banker's rounding
    return


@app.cell
def _():
    round(-12345.5)
    return


@app.cell
def _():
    round(-12344.5)
    return


@app.cell
def _():
    round(-12346.5)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
