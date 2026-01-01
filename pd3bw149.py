import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from plotly import express as px
    return pd, px


@app.cell
def _(pd):
    filename = '/Users/reuven/BambooWeekly/notebooks/data/bw-149-FluViewPhase2Data/ILINet.csv'

    df = pd.read_csv(filename, engine='pyarrow', header=1)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _():
    # How different is 2025's flu season in New York? Based on the ILINet data, create a data frame whose rows are the week numbers, whose columns are the years, and whose values consist of weighted percentage of patients reporting visits for flu-like infections in HHS region 2 (New York and New Jersey). Plot these numbers such that you can compare infection rates for the same week across years starting in 2020. Does this year's infection rate seem higher? If using Pandas 3, use the col syntax rather than lambda.
    return


@app.cell
def _(df, px):

    (
        df
        .loc[lambda df_: df_['REGION'] == 'Region 2']
        .loc[lambda df_: df_['YEAR'] >= 2020]
        .assign(YEAR = lambda df_: df_['YEAR'].astype(str))
        .pivot_table(index='WEEK',
                    columns='YEAR',
                     values='% WEIGHTED ILI')
        .pipe(px.line)
    )
    return


@app.cell
def _(df, pd, px):
    (
        df
        .loc[pd.col('REGION') == 'Region 2']
        .loc[pd.col('YEAR') >= 2020]
        .assign(YEAR = pd.col('YEAR').astype(str))
        .pivot_table(index='WEEK',
                    columns='YEAR',
                     values='% WEIGHTED ILI')
        .pipe(px.line)
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
