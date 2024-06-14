from typing import List, Optional

from progress_decorator.wrappers import CallPoint


class EndPoint:
    """An endpoint is a point in the code where we want to monitor the progress of a function or an iterable."""

    def __init__(
        self, global_call_stack: List[CallPoint], leave: Optional[bool] = None
    ) -> None:
        self.global_call_stack = global_call_stack
        self.leave = True if leave is None else leave

    def should_leave(self) -> bool:
        # If the parent call point is not left, its children should not be left either
        if len(self.global_call_stack) > 0:
            return self.leave and self.global_call_stack[-1].leave
        else:
            return self.leave
