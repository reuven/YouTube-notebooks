import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return (pd,)


@app.cell
def _():
    # datetime64 

    # - seconds (since the epoch)
    # - microseconds (us)
    # - nanoseconds (ns)

    # datetime64[s], datetime64[us], datetime64[ns]
    return


@app.cell
def _(pd):
    now = '2025-12-23 20:06:59'

    pd.to_datetime([now])
    return


@app.cell
def _(pd):
    now2 = '2025-12-23 20:06:59.0000000000012345'

    t = pd.to_datetime([now2])
    t
    return (t,)


@app.cell
def _(t):
    t.astype(int)
    return


@app.cell
def _(pd):
    filename = '/Users/reuven/Courses/Current/Data/taxi.csv'
    df = pd.read_csv(filename,
                     parse_dates=['tpep_pickup_datetime',
                                 'tpep_dropoff_datetime'],
                    engine='pyarrow')


    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
