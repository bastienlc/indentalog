import functools
from types import TracebackType
from typing import Any, Callable, Optional, Type

from rich.console import RenderableType
from rich.spinner import Spinner
from rich.table import Table

from progress_decorator.wrappers import CallPoint, EndPoint


class DecoratorCallPoint(CallPoint):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.spinner = Spinner("dots", text=self.name)

    def render(self) -> RenderableType:
        if self.finished:
            text = self.offset()
            text.append(f"✔ {self.name}", style="green")
            return text
        elif self.depth == 0:
            return self.spinner
        else:
            grid = Table.grid()
            grid.add_column(justify="left")
            grid.add_column(justify="left")
            grid.add_row(self.offset(), self.spinner)
            return grid


class DecoratorEndPoint(EndPoint):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __call__(self, func: Callable) -> Callable:
        if self.name is None:
            self.name = func.__name__

        @functools.wraps(func)
        def wrap(*args, **kwargs) -> Any:
            # Create a new call point
            call_point = DecoratorCallPoint(
                monitor=self.monitor,
                leave=self.leave,
                name=self.name,
            )
            # Call the function
            output = func(*args, **kwargs)
            # Stop the call point
            call_point.stop()

            return output

        return wrap

    def __enter__(self):
        if self.name is None:
            self.name = "Context manager"
        self.call_point = DecoratorCallPoint(
            monitor=self.monitor,
            leave=self.leave,
            name=self.name,
        )

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ):
        self.call_point.stop()
