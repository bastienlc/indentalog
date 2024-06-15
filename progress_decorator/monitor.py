from typing import Callable, Iterable, List, Optional

from rich.console import Console, group
from rich.live import Live

from progress_decorator.wrappers import CallPoint, FunctionEndPoint, IterableEndPoint


class Monitor:
    call_stack: List[CallPoint] = []
    console = Console()

    def __init__(self) -> None:
        self.live = Live(
            refresh_per_second=10,
            console=self.console,
            get_renderable=self.render,
        )
        self.live.start()

    def __del__(self) -> None:
        self.live.stop()

    @group()
    def render(self):
        for call_point in self.call_stack:
            yield call_point.render()

    def __call__(
        self,
        arg1: Optional[Iterable] = None,
        leave: bool = True,
        name: Optional[str] = None,
    ) -> Callable[[Callable], Callable]:
        if arg1 is None:
            endpoint = FunctionEndPoint(
                global_call_stack=self.call_stack, leave=leave, name=name
            )
            return endpoint

        elif isinstance(arg1, Iterable):
            endpoint = IterableEndPoint(
                iterable=arg1, global_call_stack=self.call_stack, leave=leave, name=name
            )
            return endpoint

        else:
            raise ValueError(f"Invalid argument {arg1} for Monitor class.")


monitor = Monitor()
