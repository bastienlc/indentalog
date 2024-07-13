from time import sleep

from progress_decorator import monitor


@monitor()
def my_first_function():
    # Your code here
    sleep(1)
    pass


def my_second_function():
    for i in monitor(range(10)):
        # Your code here
        sleep(0.1)
        pass


my_first_function()
my_second_function()
