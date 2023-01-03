This is a basic template for cli apps in Python.

usage: `python main.py -h`

# packages

## installing

required `pip install pip-tools`

then for normal dependencies `pip-sync requirements.txt` or for dev `pip-sync requirements-dev.txt`

## add new package

1. add to requirements.in
2. then run `pip-compile requirements.in && pip-sync requirements.txt`

For dev dependencies:

1. add to requirements-dev.in
2. run `pip-compile requirements.in requirements-dev.in -o requirements-dev.txt && pip-sync requirements-dev.txt`

## update

run `pip-compile --upgrade requirements.in && pip-sync requirements.txt`

Dev dependencies:

run `pip-compile --upgrade requirements.in requirements-dev.in -o requirements-dev.txt && pip-sync requirements-dev.txt`
