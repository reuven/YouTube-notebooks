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
    filename = '/Users/reuven/Courses/Current/data/nyc_taxi_2025-11.parquet'

    df = pd.read_parquet(filename)[['tpep_pickup_datetime',
                                    'tpep_dropoff_datetime',
                                    'passenger_count',
                                    'trip_distance',
                                    'total_amount']]

    df
    return (df,)


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df):
    (
        df
        .sort_values(['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
        .assign(tpep_pickup_datetime = lambda df_: df_['tpep_pickup_datetime'].dt.tz_localize('US/Eastern', ambiguous='infer'),
                tpep_dropoff_datetime = lambda df_: df_['tpep_dropoff_datetime'].dt.tz_localize('US/Eastern', ambiguous='infer'))
        .info()
    )
    return


@app.cell
def _(df):
    (
        df
        .assign(tpep_pickup_datetime = lambda df_: df_['tpep_pickup_datetime'].dt.tz_localize('US/Eastern'),
                tpep_dropoff_datetime = lambda df_: df_['tpep_dropoff_datetime'].dt.tz_localize('US/Eastern'))
        ['tpep_pickup_datetime'].dt.tz
    )
    return


@app.cell
def _(df):
    (
        df
        .assign(tpep_pickup_datetime = lambda df_: df_['tpep_pickup_datetime'].dt.tz_localize('US/Eastern'),
                tpep_dropoff_datetime = lambda df_: df_['tpep_dropoff_datetime'].dt.tz_localize('US/Eastern'))
        .info()
    )
    return


@app.cell
def _(df):
    (
        df
        .assign(tpep_pickup_datetime = lambda df_: df_['tpep_pickup_datetime'].dt.tz_localize('US/Eastern'),
                tpep_dropoff_datetime = lambda df_: df_['tpep_dropoff_datetime'].dt.tz_localize('US/Eastern'))
        .loc[lambda df_: df_['tpep_dropoff_datetime'] < df_['tpep_pickup_datetime']]
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
