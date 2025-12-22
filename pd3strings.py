import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
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
    df.head()
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df):
    df['Vehicle Color'].value_counts().head(10)
    return


@app.cell
def _(df):
    df.groupby('Vehicle Color')['Registration State'].count()
    return


@app.cell
def _(df, pd):
    df.loc[0, 'Plate ID'] = pd.NA 
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df.loc[0, 'Plate ID']
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
