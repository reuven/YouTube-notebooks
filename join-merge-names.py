import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    import pandas as pd
    from pandas import Series, DataFrame
    return


app._unparsable_cell(
    r"""
    people = DataFrame({'first_name': })
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
