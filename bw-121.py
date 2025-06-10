import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    1. Read the NIH data into a Pandas data frame. Which 15 institutions had the greatest dollar amount of grants (`usa_total_award`) terminated? Display each institution in "title" format (i.e., with each word starting with a capital letter) and with each dollar amount with commas before every three digits.
    2. Repeat this task with the NSF data, looking at `nsf_total_budget`. You'll want the `nsf_startdate` column to be treated as a `datetime` value. Do you see any overlap between the NIH and NSF results? What issues might we have in trying to combine the two data sets?

    """
    )
    return


@app.cell
def _():
    import pandas as pd

    nih_filename = '/Users/reuven/Downloads/nih_terminations_airtable.csv'
    nsf_filename = '/Users/reuven/Downloads/nsf_terminations_airtable.csv'
    return nih_filename, nsf_filename, pd


@app.cell
def _(nih_filename, pd):
    ( pd
      .read_csv(nih_filename)
      .assign(org_name = lambda df_: df_['org_name'].str.title() ) 
      .groupby('org_name')['usa_total_award'].sum()
      .nlargest(15)
      .map(lambda x: f'${x:,.2f}')
    )
    return


@app.cell
def _(nsf_filename, pd):
    ( pd
      .read_csv(nsf_filename)
      .assign(nsf_total_budget = lambda df_: df_['nsf_total_budget'].str.replace('$', '').astype(int),
              org_name = lambda df_: df_['org_name'].str.title() ) 
      .groupby('org_name')['nsf_total_budget'].sum()
      .nlargest(15)
      .map(lambda x: f'${x:,.2f}')
    )
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
