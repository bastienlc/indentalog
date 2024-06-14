from typing import List, Self

from rich.console import RenderableType
from rich.text import Text


class CallPoint:
    """A callpoint is a point in the call stack where we want to monitor the progress of a function or an iterable. It is created by an endpoint."""

    def __init__(self, global_call_stack: List[Self], leave: bool) -> None:
        self.global_call_stack = global_call_stack
        self.finished = False
        self.leave = leave
        self.start()
        self.depth = self._compute_depth()

    def render(self) -> RenderableType:
        pass

    def start(self) -> None:
        self.global_call_stack.append(self)

    def stop(self) -> None:
        self.finished = True
        if not self.leave:
            self.global_call_stack.remove(self)

    def _compute_depth(self) -> int:
        depth = 0
        for call_point in self.global_call_stack:
            if call_point == self:
                return depth
            elif not call_point.finished:
                depth += 1

        raise ValueError("Expected to find the current call point in the stack.")

    def depths_to_mark(self) -> bool:
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
        depths_to_mark = self.depths_to_mark()
        for depth in range(self.depth)[: self.depth]:
            if depths_to_mark[depth]:
                text.append(" │")
            else:
                text.append("  ")

        if depths_to_mark[self.depth]:
            text.append(" ├")
        else:
            text.append(" └")

        return text
