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

    df = (
          pd
          .read_parquet(filename)
          .assign(date = lambda df_: pd.to_datetime(df_['Issue Date'], format='%m/%d/%Y %I:%M:%S %p'))
          .set_index('date')
          .drop(columns='Issue Date')
    )

    df
    return (df,)


@app.cell
def _(df):
    df['Summons Number'].count()
    return


@app.cell
def _(df):
    # how many summons per vehicle make?

    df.groupby('Vehicle Make')['Summons Number'].count().sort_values(ascending=False)
    return


@app.cell
def _(df):
    # how many summons were there per week?

    (
        df
        .loc['2020']
        .resample('3W')['Summons Number'].count()
    )
    return


@app.cell
def _(df):
    (
        df
        .loc['2020']
        .resample('2M')['Summons Number'].count()
    )
    return


@app.cell
def _(df):
    (
        df
        .loc['2020']
        .resample('1SM')['Summons Number'].count()
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
