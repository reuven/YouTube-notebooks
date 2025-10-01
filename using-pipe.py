import marimo

__generated_with = "0.16.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from plotly import express as px

    return pd, px


@app.cell
def _(pd, px):
    # let's create a histogram of the trip_distance column

    (
        pd
        .read_csv('taxi.csv')
        ['trip_distance']
        .pipe(lambda s_: px.histogram(s_))
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
