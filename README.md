# Clock Keeper
A very minimalistic python module that lets you track the time your code snippets take to run.

This package is available on PyPI! Run the following command on your terminal to use it in your project.

```
pip install clock-keeper
```
## Usage example is as follows -
#### Importing Class from module.
```python
from clock_keeper.utility import Timer
```

#### Instantiating timer object.
```python
timer = Timer()
```

#### Starting and ending keeping time.
```python
timer.markStart()

for loop in lengthy_task:
    # Computing the meaning of life.

timer.markEnd()
```

#### Output -
```
started processing: 2022-01-19 16:24:57.534867
done processing: 2022-01-19 16:25:05.282381
this operation took: 0:00:07.747514
```

### Contributions
Feel free to fork this project and add testing functionality and better terminal logging (especially if you want it in your production use cases).

Cheers,
Rajdeep. <3
