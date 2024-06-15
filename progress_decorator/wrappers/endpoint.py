from typing import List, Optional

from progress_decorator.wrappers import CallPoint


class EndPoint:
    """An endpoint is a point in the code where we want to monitor the progress of a function or an iterable."""

    def __init__(
        self,
        global_call_stack: List[CallPoint],
        leave: bool,
        name: Optional[str] = None,
    ) -> None:
        self.global_call_stack = global_call_stack
        self.leave = leave
        self.name = name
