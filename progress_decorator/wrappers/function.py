import functools
from typing import Any, Callable

from rich.spinner import Spinner
from rich.table import Table

from progress_decorator.wrappers import CallPoint, EndPoint


class FunctionCallPoint(CallPoint):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.spinner = Spinner("dots", text=self.name)

    def render(self) -> Spinner:
        if self.finished:
            text = self.offset()
            text.append(f"✔ {self.name}", style="green")
            return text
        else:
            grid = Table.grid()
            grid.add_column(justify="left")
            grid.add_column(justify="left")
            grid.add_row(self.offset(), self.spinner)
            return grid


class FunctionEndPoint(EndPoint):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __call__(self, func: Callable) -> Callable:
        if self.name is None:
            self.name = func.__name__

        @functools.wraps(func)
        def wrap(*args, **kwargs) -> Any:
            # Create a new call point
            call_point = FunctionCallPoint(
                global_call_stack=self.global_call_stack,
                leave=self.leave,
                name=self.name,
            )
            # Call the function
            output = func(*args, **kwargs)
            # Stop the call point
            call_point.stop()

            return output

        return wrap
