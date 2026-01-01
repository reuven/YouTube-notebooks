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
    df1 = pd.DataFrame([[10, 20, 30],
                      [40, 50, 60]],
                     index=list('mn'),
                     columns=list('zyx'))

    df2 = pd.DataFrame([[100, 200, 300],
                      [400, 500, 600]],
                     index=list('cd'),
                     columns=list('xyz'))
    return df1, df2


@app.cell
def _(df1):
    df1
    return


@app.cell
def _(df2):
    df2
    return


@app.cell
def _(df1, df2, pd):
    pd.concat([df1, df2], sort=True)
    return


@app.cell
def _(df1, df2, pd):
    # combine them side-to-side

    pd.concat([df1, df2], axis='columns')
    return


@app.cell
def _(df1, df2, pd):
    pd.concat([df1, df2], axis='columns', sort=True)
    return


@app.cell
def _(pd):
    tdf1 = pd.DataFrame({'a': [1, 2, 3]},
                       index=pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-05']))

    tdf2 = pd.DataFrame({'b': [10, 20, 30]},
                       index=pd.to_datetime(['2000-01-02', '2000-01-03', '2000-01-04']))

    return tdf1, tdf2


@app.cell
def _(tdf1):
    tdf1
    return


@app.cell
def _(tdf2):
    tdf2
    return


@app.cell
def _(pd, tdf1, tdf2):
    pd.concat([tdf1, tdf2], sort=True)
    return


@app.cell
def _(pd, tdf1, tdf2):
    pd.concat([tdf1, tdf2], axis='columns', sort=False)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
