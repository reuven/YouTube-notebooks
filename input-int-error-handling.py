import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    x = input('Enter your favorite number: ').strip()

    try:
        n = int(x)
        print(f'{n} * 5 = {n*5}')
    except ValueError as e:
        print(f'{x} is not numeric: {e}')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
