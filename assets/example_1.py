from time import sleep

from indentalog import ilog


@ilog()
def my_first_function():
    # Your code here
    sleep(1)
    pass


def my_second_function():
    for i in ilog(range(10)):
        # Your code here
        sleep(0.1)
        pass


my_first_function()
my_second_function()
