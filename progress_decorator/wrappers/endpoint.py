from typing import Optional

from progress_decorator.wrappers.callpoint import PartialMonitor


class EndPoint:
    """An endpoint is a point in the code where we want to monitor the progress of a function or an iterable."""

    def __init__(
        self,
        monitor: PartialMonitor,
        leave: bool,
        name: Optional[str] = None,
    ) -> None:
        self.monitor = monitor
        self.leave = leave
        self.name = name
