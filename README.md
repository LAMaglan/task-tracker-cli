# Intro

A CLI that creates a todo table in the terminal using typer, rich, and sqlite3 (opens and closes a database object)
<br>
Original code can be found [here](https://github.com/python-engineer/python-fun/tree/master/todocli-tutorial)
<br>
Youtube tutorial can be found [here](https://www.youtube.com/watch?v=ynd67UwG_cI)

# Step 0 - Getting started

Optional: Create a virtual environment
e.g.
<br>
`conda create -n task-tracker-env python=3.9`

activate environment
<br>
`conda activate <name-of-env>`

Install rich and typer
<br>
`pip install rich typer`

# Step 1: main file

**todocli.py**
<br>
type hints are necessary (or strongly advised?) in _typer_ functions
<br>
(see file for comments)
after the bare bones (see commit), can see options by doing
<br>
`python todocli.py --help`
<br>
and further with
<br>
`python todocli.py <some paramater> --help`
<br>
with bare bones "app", you can add tasks that are shown in terminal like this:
<br>
`python todocli.py add "Todo1" "SomeTask"`
<br>
after defining start of show function, can show the TODO table by doing:
<br>
`python todocli.py show`
<br>

# Step 2: model and databse

model: create a Todo class
defined an own `__repr__` for "prettier" printing

database: create table in accordance with model.ply
use paramater substitution syntax (see insert_todo function) instead of
<br>
f-strings to avoid SQL-injection attack.
<br>
This has functions that get used in the various typer functions todocli.py

update the todocli.py to use functions defined in database.py

Once finished, can now after adding items do
<br>
`python todocli.py complete <row number>`
<br>
to display check mark for a given item
