import marimo

__generated_with = "0.14.7"
app = marimo.App(width="medium")


@app.cell
def _():
    s = 'abcdefghijklmnopqrstuvwxyz'


    return (s,)


@app.cell
def _(s):
    # if I want a single character from s, I can use [] and put an index inside of them
    s[10]
    return


@app.cell
def _(s):
    i = 10
    s[i]
    return


@app.cell
def _(s):
    # what if I want all of the characters from index 10 up to (and not including) index 20?
    # for that, I can use a *slice*

    s[10:20]    # notice that it's from:to, where the "to" is "up to and not including"
    return


@app.cell
def _(s):
    # what if I want from the start of the string until (not including) index 20?
    s[0:20]
    return


@app.cell
def _(s):
    # but I can also leave out the initial index!
    s[:20]
    return


@app.cell
def _(s):
    # what about the end?
    s[10:25]
    return


@app.cell
def _(s):
    # two options for including the final character
    # One: go past the final index!

    s[10:26]
    return


@app.cell
def _(s):
    s[10:2600]
    return


@app.cell
def _(s):
    # other way to do it -- leave off the ending index
    s[10:]
    return


@app.cell
def _(s):
    # get a copy of a string with 
    s[:]
    return


@app.cell
def _(s):
    # there is actually a third argument you can give to the slice syntax -- the step size
    s[10:20:2]  # this means: start at 10, end before 20, and step size of 2
    return


@app.cell
def _(s):
    # people often ask how to iterate over a string, every other character
    for one_character in s[::2]:   # from the start, to the end, step size 2
        print(one_character)
    return


@app.cell
def _(s):
    # slice syntax with : only works inside of []!
    my_slice = slice(10,20)  # creating a slice object -- the same as saying [10:20]

    s[my_slice]  
    return


@app.cell
def _(s):
    # what if I want to go backwards?
    s[20:10]
    return


@app.cell
def _(s):
    s[20:10:-1]  # from 20, to (not including) 10, with a step size of -1
    return


@app.cell
def _(s):
    s[::-1]
    return


@app.cell
def _():
    mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    mylist[3:5]
    return


@app.cell
def _():
    d = {'a':10, 'b':20, 'c':30}

    d[slice('a', 'b')]
    return (d,)


@app.cell
def _(d):
    d['a':'b']
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
