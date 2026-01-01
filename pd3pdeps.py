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
    filename = '/Users/reuven/Courses/Current/Data/olympic_athlete_events.csv'

    df = pd.read_csv(filename,
                    dtype={'Team':'category',
                          'Season':'category'})

    df
    return (df,)


@app.cell
def _(df):
    df.groupby('Team')['Height'].mean()
    return


@app.cell
def _(pd):
    s = pd.Series([10, 20, 30, 40, 50])
    s.loc[2] = 'hello'
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
