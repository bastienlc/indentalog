from typing import Iterable

from rich.progress import Progress
from rich.spinner import Spinner
from rich.table import Table
from rich.text import Text

from progress_decorator.wrappers import CallPoint, EndPoint


class IterableCallPoint(CallPoint):
    def __init__(self, total: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.total = total
        self.progress = Progress()
        self.task_id = self.progress.add_task("", total=total)
        self.spinner = Spinner("dots")

    def render(self) -> Progress:
        self.progress.update(self.task_id)
        text = Text()
        grid = Table.grid()
        grid.add_column(justify="left")
        grid.add_column(justify="left")
        grid.add_column(justify="left")

        if self.finished:
            text.append(f"✔ {self.name}", style="green")
            grid.add_row(
                self.offset(),
                text,
                self.progress,
            )
        else:
            text.append(f" {self.name}")
            grid.add_column(justify="left")
            grid.add_row(
                self.offset(),
                self.spinner,
                text,
                self.progress,
            )

        return grid

    def clear_call_stack(self) -> None:
        if not self.progress.finished:
            while self.global_call_stack[-1] != self:
                self.global_call_stack.pop()

    def advance(self) -> None:
        self.progress.advance(self.task_id)
        self.clear_call_stack()


class IterableEndPoint(EndPoint):
    def __init__(
        self,
        iterable: Iterable,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.iterable = iterable
        if self.name is None:
            self.name = ""

    def __iter__(self):
        call_point = IterableCallPoint(
            total=len(self.iterable),
            global_call_stack=self.global_call_stack,
            leave=self.leave,
            name=self.name,
        )
        for item in self.iterable:
            yield item
            call_point.advance()
        call_point.stop()
