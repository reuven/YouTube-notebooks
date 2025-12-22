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
    df.head()
    return


@app.cell
def _(df):
    # How can I find out how many cars of each make got a ticket?
    # but I'm only interested in cars from NY and PA
    # I'm only interested in cars that are black

    def only_ny_pa_vehicles(df_):
        return df_['Registration State'].isin(['NY', 'PA'])

    def only_black_vehicles(df_):
        return df_['Vehicle Color'] == 'BLACK'


    (
        df
        .loc[  only_ny_pa_vehicles ]
        .loc[  only_black_vehicles ]
        ['Vehicle Make']
        .value_counts()
    )
    return


@app.cell
def _(df):

    (
        df
        .loc[  lambda df_: df_['Registration State'].isin(['NY', 'PA']) ]
        .loc[  lambda df_: df_['Vehicle Color'] == 'BLACK' ]
        ['Vehicle Make']
        .value_counts()
    )
    return


@app.cell
def _(df):
    # What streets are the locations for the most Kia parking tickets where there person is > 0 feet from the curb?

    (
        df
        .loc[ lambda df_: df_['Feet From Curb'] > 0]
        .loc[ lambda df_: df_['Vehicle Make'] == 'KIA']
        .loc[ lambda df_: df_['Vehicle Color'] == 'BLACK']
        ['Street Name']
        .value_counts()
    )
    return


@app.cell
def _(df):
    # I want to know whether people get more citations at even-numbered homes or odd-numbered homes

    (
        df
        .dropna(subset='House Number')
        .loc[lambda df_: df_['House Number'].str.isdigit()]
        .assign(is_even = lambda df_: df_['House Number'].astype(int) % 2 == 0)
        ['is_even']
        .value_counts(normalize=True)
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
