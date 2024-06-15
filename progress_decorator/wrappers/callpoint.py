from typing import List, Optional, Self

from rich.console import RenderableType
from rich.text import Text


class CallPoint:
    """A callpoint is a point in the call stack where we want to monitor the progress of a function or an iterable. It is created by an endpoint."""

    def __init__(
        self, global_call_stack: List[Self], leave: bool, name: Optional[str] = None
    ) -> None:
        self.global_call_stack = global_call_stack
        self.leave = leave
        self.name = name

        self.start()

    def render(self) -> RenderableType:
        pass

    def start(self) -> None:
        self.finished = False
        self.global_call_stack.append(self)
        self.depth = self._compute_depth()

    def stop(self) -> None:
        self.finished = True
        if not self._should_leave():
            self.global_call_stack.remove(self)

    def _compute_depth(self) -> int:
        depth = 0
        for call_point in self.global_call_stack:
            if call_point == self:
                return depth
            elif not call_point.finished:
                depth += 1

        raise ValueError("Expected to find the current call point in the stack.")

    def _should_leave(self) -> bool:
        # If the parent call point is not left, its children should not be left either.
        # We only need to check the previous call point because:
        # 1. Either it is the parent call point, in which case we can check if has leave=True
        # 2. Or it is a sibling call point that has been left, which means that the parent
        #    call point has leave=True
        if len(self.global_call_stack) > 1:
            previous_call_point = self.global_call_stack[
                self.global_call_stack.index(self) - 1
            ]
            return self.leave and previous_call_point.leave
        else:
            return self.leave

    def _depths_to_mark(self) -> bool:
        visits = [0] * (self.depth + 1)
        broken_flow = False
        for call_point in self.global_call_stack[
            self.global_call_stack.index(self) + 1 :
        ]:
            if call_point.depth > self.depth:
                continue
            elif call_point.depth == self.depth:
                if not broken_flow:
                    visits[self.depth] += 1
            else:
                visits[call_point.depth] += 1
                broken_flow = True

        return [visit > 0 for visit in visits]

    def offset(self) -> Text:
        text = Text()
        if self.depth == 0:
            return text

        depths_to_mark = self._depths_to_mark()
        for depth in range(self.depth)[1:]:
            if depths_to_mark[depth]:
                text.append(" │")
            else:
                text.append("  ")

        if depths_to_mark[self.depth]:
            text.append(" ├")
        else:
            text.append(" └")

        return text
