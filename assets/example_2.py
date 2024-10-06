from time import sleep

from indentalog import ilog


@ilog()
def my_inner_function():
    # Your code here
    sleep(0.5)
    pass


def my_main_function():
    for i in ilog(range(3), name="Main function"):
        # Your code here
        sleep(0.1)
        my_inner_function()
        sleep(0.5)
        pass


my_main_function()
