import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    return np, pd


@app.cell
def _(np, pd):
    np.random.seed(0)
    df = pd.DataFrame(np.random.randint(0, 1000, [4,5]),
                      index=list('abcd'),
                      columns=list('vwxyz'))
    df['names'] = ['Alice', 'Bob', 'Carol', 'David']

    df.loc['a', 'w'] = np.nan
    df.loc['b', 'x'] = np.nan
    df.loc['c', 'y'] = np.nan
    df.loc['c', 'y'] = np.nan
    df.loc['d', 'z'] = np.nan

    df
    return (df,)


@app.cell
def _():
    # df.set_index('names', inplace=True)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _():
    # df.interpolate(inplace=True)
    return


@app.cell
def _(df):
    df.interpolate()
    return


@app.cell
def _(df):
    df.set_index('names').interpolate(inplace=True)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
