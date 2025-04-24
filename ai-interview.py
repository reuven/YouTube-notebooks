import marimo

__generated_with = "0.12.9"
app = marimo.App(width="medium")


@app.cell
def _():
    # ask the user their name
    # if the name matches yours, say something nice
    # if the name doesn't match yours, then say something snarky

    name = input('Enter your name: ')

    if name == 'Reuven':
        print('Hi, boss!')
        print('Nice to see you here!')
    else:
        print(f'Hello, {name} -- who are you?')
    return (name,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
