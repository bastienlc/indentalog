# progress-decorator

An easy-to-use progress bar decorator for Python functions and loops.

## Getting Started

**progress-decorator** will be available on PyPI once it reaches a stable version. For now, you can install it from the source code.

```bash
git clone git@github.com:bastienlc/progress-decorator.git
poetry install
```

**progress-decorator** has the simplest API possible. Just import the `monitor` object and use it either as a decorator, as an iterator wrapper or as a context manager.

```python
from progress_decorator import monitor

@monitor()
def my_first_function():
    # Your code here
    pass

def my_second_function():
    for i in monitor(range(10)):
        # Your code here
        pass

my_first_function()
my_second_function()
```

![GIF for the first example.](./assets/example_1.gif)

The main advantage of **progress-decorator** is that it keeps track of the call stack, which allows displaying the progress of nested functions or loops.

```python
from progress_decorator import monitor

@monitor()
def my_inner_function():
    # Your code here
    pass

def my_main_function():
    for i in monitor(range(3), name="Main function"):
        # Your code here
        my_inner_function()
        pass

my_main_function()
```

![GIF for the first example.](./assets/example_2.gif)


### Future features
- [ ] Passing data to the endpoints
- [ ] Support for custom styles or themes
