import marimo

__generated_with = "0.14.9"
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
def _(pd):
    taxi_df = pd.read_csv('/Users/reuven/Courses/Current/Data/nyc_taxi_2019-07.csv', engine='pyarrow')
    return (taxi_df,)


@app.cell
def _(taxi_df):
    taxi_df.shape
    return


@app.cell
def _(pd, taxi_df):
    # calculate average cost per mile

    for i in range(len(taxi_df)):
        if taxi_df[i, 'trip_distance']:
            taxi_df.loc[i, 'dollars_per_mile'] = taxi_df.loc[i, 'total_amount'] / taxi_df.loc[i, 'trip_distance']
        else:
            taxi_df.loc[i, 'dollars_per_mile'] = pd.NA 
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
