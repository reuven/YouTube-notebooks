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
    filename = '/Users/reuven/Courses/Current/Data/nyc-parking-violations-2020.parquet'

    df = pd.read_parquet(filename)
    return (df,)


@app.cell
def _(df):
    df.shape
    return


@app.cell
def _(df):
    df.dtypes
    return


@app.cell
def _(df):
    # request a row -- index 0

    df.loc[0]
    return


@app.cell
def _(df):
    df.loc[0].loc['Summons Number'] = 1
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df.loc[0, 'Summons Number'] = 1
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
