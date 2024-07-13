# progress-decorator

An easy-to-use progress bar decorator for Python functions and loops.

## Getting Started

**progress-decorator** is available on PyPI and can be installed using pip.

```bash
pip install progress-decorator
```

**progress-decorator** has the simplest API possible. Just import the `monitor` object and use it either as a decorator, or as a wrapper.

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


### Future features
- [ ] Endpoint on a single function call (and not a decorator)
- [ ] Support for class methods
- [ ] Endpoint without anything else (i.e. no spinner)
- [ ] Passing data to the endpoints
- [ ] Support for custom styles or themes
