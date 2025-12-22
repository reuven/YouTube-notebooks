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
def _(df, pd):
    (
        df
        .loc[  pd.col('Registration State').isin(['NY', 'PA']) ]
        .loc[  pd.col('Vehicle Color') == 'BLACK' ]
        ['Vehicle Make']
        .value_counts()
    )
    return


@app.cell
def _(df, pd):

    (
        df
        .loc[ pd.col('Feet From Curb') > 0]
        .loc[ pd.col('Vehicle Make') == 'KIA']
        .loc[ pd.col('Vehicle Color') == 'BLACK']
        ['Street Name']
        .value_counts()
    )
    return


@app.cell
def _(df, pd):

    (
        df
        .dropna(subset='House Number')
        .loc[ pd.col('House Number').str.isdigit()]
        .assign(is_even = pd.col('House Number').astype(int) % 2 == 0)
        ['is_even']
        .value_counts(normalize=True)
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
