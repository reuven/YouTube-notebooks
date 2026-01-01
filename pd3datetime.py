import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    return (pd,)


@app.cell
def _(pd):
    now = '2025-12-23 20:06:59'

    pd.to_datetime([now])
    return


@app.cell
def _(pd):
    # now2 = '2025-12-23 20:06:59.0000000000012345'

    now2 = '2025-12-23 20:06:59'
    t = pd.to_datetime([now2])
    t
    return (t,)


@app.cell
def _(t):
    t.unit
    return


@app.cell
def _(t):
    t.astype(int)
    return


@app.cell
def _(pd):
    filename = '/Users/reuven/Courses/Current/Data/taxi.csv'
    df = pd.read_csv(filename,
                     parse_dates=['tpep_pickup_datetime',
                                 'tpep_dropoff_datetime'],
                    engine='pyarrow')

    df
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
