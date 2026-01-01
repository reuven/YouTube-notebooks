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
    filename = '/Users/reuven/Courses/Current/data/olympic_athlete_events.csv'

    seasons_category = pd.CategoricalDtype(['Winter', 'Summer', 'Spring', 'Autumn'])

    df = pd.read_csv(filename,
                    dtype={'Season':seasons_category})

    df
    return (df,)


@app.cell
def _(df):
    df.info(memory_usage='deep')
    return


@app.cell
def _():
    # 158.9 MB  # 144.9
    return


@app.cell
def _(df):
    df.groupby('Season', observed=False)['Height'].mean()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
