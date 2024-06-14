from typing import Iterable, List, Optional

from rich.progress import Progress
from rich.spinner import Spinner
from rich.table import Table
from rich.text import Text

from progress_decorator.wrappers import CallPoint, EndPoint


class IterableCallPoint(CallPoint):
    def __init__(
        self, global_call_stack: List[CallPoint], leave: bool, name: str, total: int
    ) -> None:
        super().__init__(global_call_stack, leave)
        self.name = name
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
        global_call_stack: List[CallPoint],
        iterable: Iterable,
        leave: Optional[bool] = None,
        name: Optional[str] = None,
    ) -> None:
        super().__init__(global_call_stack, leave)
        self.iterable = iterable
        self.name = name or ""

    def __iter__(self):
        call_point = IterableCallPoint(
            self.global_call_stack, self.should_leave(), self.name, len(self.iterable)
        )
        for item in self.iterable:
            yield item
            call_point.advance()
        call_point.stop()
