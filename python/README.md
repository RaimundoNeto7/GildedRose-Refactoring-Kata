# GildedRose Refactoring Kata (Python)

I'm using Pipenv to manage black, flake8 and pytest dev dependencies. 

___

### Run with pipenv

How to run black formatter:
```
pipenv run black ./src ./tests --exclude '/*.git'
```

How to run tests:
```
pipenv run pytest . -v
```

___

### Run with pytest installed locally
```
pytest . -v
```