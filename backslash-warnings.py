import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _():
    s = 'Hello!\nGoodbye'
    print(s)   # \n is turned into the "newline character"
    return (s,)


@app.cell
def _(s):
    len(s)
    return


@app.cell
def _():
    # what if I want to print the literal \n?

    print('Hello!\\nGoodbye')   # the first \ escapes the second one, and thus we get 1 \
    return


@app.cell
def _():
    print('a\tb')
    return


@app.cell
def _():
    # what happens if I use \ before a character that doesn't have any special meaning?

    text = r'a\ob'
    print(text)
    return (text,)


@app.cell
def _(text):
    len(text)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
