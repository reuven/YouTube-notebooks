import marimo

__generated_with = "0.12.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""1. Start a Marimo notebook. Import the data into a data frame, removing rows in which the partnerDesc is 'World'. Keep only the columns refYear, reporterDesc, flowDesc, partnerDesc, and fobvalue. Without using any code, sort the rows by the fobvalue column. Which country imports the greatest dollar amount of products, and from where?""")
    return


@app.cell
def _():
    import pandas as pd

    filename = '/Users/reuven/BambooWeekly/notebooks/data/TradeData.csv'

    df = (pd
          .read_csv(filename,
                    usecols=['refYear', 'reporterDesc', 
                             'flowDesc', 'partnerDesc', 
                             'fobvalue'])
          .loc[lambda df_: df_['partnerDesc'] != 'World']
         )

    df
    return df, filename, pd


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""2. Define n to be 10. Create a bar plot showing the n countries from which the US imported the most in 2024, and the fobvalue. Create a second bar plot showing the n countries to which the US exported the most in 2024, along with the fobvalue. What happens when you update n?""")
    return


@app.cell
def _(mo):
    n = mo.ui.slider(1, 50)
    n
    return (n,)


@app.cell
def _(df, n):
    (
        df
        .loc[lambda df_: df_['refYear'] == 2024]
        .loc[lambda df_: df_['reporterDesc'] == 'USA']
        .loc[lambda df_: df_['flowDesc'] == 'Import']
        .set_index('partnerDesc')
        ['fobvalue']
        .nlargest(n.value)
        .plot.bar()
    )
    return


@app.cell
def _(df, n):
    (
        df
        .loc[lambda df_: df_['refYear'] == 2024]
        .loc[lambda df_: df_['reporterDesc'] == 'USA']
        .loc[lambda df_: df_['flowDesc'] == 'Export']
        .set_index('partnerDesc')
        ['fobvalue']
        .nlargest(n.value)
        .plot.bar()
    
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
