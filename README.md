# indentalog

An easy-to-use progress logger for Python. **indentalog** allows you to display the progress of your functions and loops in a clean and readable way, by keeping track of the call stack. It uses [rich](https://github.com/Textualize/rich) under the hood to provide a beautiful and customizable output.

## Getting Started

**indentalog** is available on PyPI. It is still in early development, so you may encounter some bugs. If you do, please open an issue on github.

```bash
pip install indentalog
```

**indentalog** aims to make logging your script's progress as easy as possible. Just import the `ilog` object and use it either as a **decorator**, as an iterator **wrapper** or as a **context manager**.

```python
from indentalog import ilog

@ilog()
def my_first_function():
    # Your code here
    pass

def my_second_function():
    for i in ilog(range(10)):
        # Your code here
        pass

my_first_function()
my_second_function()
```

![GIF for the first example.](https://raw.githubusercontent.com/bastienlc/indentalog/master/assets/example_1.gif)

**indentalog** keeps track of the call stack, which allows displaying the progress of nested functions or loops without getting lost in the output.

```python
from indentalog import ilog

@ilog()
def my_inner_function():
    # Your code here
    pass

def my_main_function():
    for i in ilog(range(3), name="Main function"):
        # Your code here
        my_inner_function()
        pass

my_main_function()
```

![GIF for the second example.](https://raw.githubusercontent.com/bastienlc/indentalog/master/assets/example_2.gif)

The real magic happens in more complex cases, where the imperative use of `ilog` results in a clean and readable output.

```python
from indentalog import ilog

@ilog(name="Training")
def train():
    for epoch in ilog(range(2), name="Epochs"):
        for batch in ilog(range(5), name="Train batches"):
            with ilog(name="Forward pass"):
                # Your code here
                pass
                sleep(0.2)
            with ilog(name="Backward pass"):
                # Your code here
                pass
                sleep(0.2)
            sleep(0.1)

        for batch in ilog(range(5), name="Validation batches"):
            with ilog(name="Forward pass"):
                # Your code here
                pass
                sleep(0.2)
            with ilog(name="Compute metrics"):
                # Your code here
                pass
                sleep(0.2)
            sleep(0.1)

with ilog(name="Initializing model and data"):
    # Your code here
    pass

train()
```

![GIF for the third example.](https://raw.githubusercontent.com/bastienlc/indentalog/master/assets/example_3.gif)

## Contributing

Contributions are welcome! If you have any idea or suggestion, please open an issue on github. This project is still in early development, so there is a lot of room for improvement.

**Installation**

```bash
git clone git@github.com:bastienlc/indentalog.git
cd indentalog
make install
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
