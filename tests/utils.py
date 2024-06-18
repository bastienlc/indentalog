import filecmp
import os
import shutil
from types import TracebackType
from typing import Optional, Type

import pytest
from rich.console import Console

from progress_decorator import monitor
from progress_decorator.monitor import Monitor

FIXTURES = "tests/fixtures"
OUTPUTS = "tests/outputs"


@pytest.fixture()
def cleanup():
    os.makedirs(OUTPUTS, exist_ok=True)
    yield
    shutil.rmtree(OUTPUTS)


class MonitorGetter(Monitor):
    """A helper class to get a clean monitor for each test. It deletes the previous monitor and starts a new one, without having two rich lives running at the same time."""

    auto_start = False

    def __enter__(self) -> Monitor:
        monitor.__del__()
        self.__init__()
        self.live.start()
        return self

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> bool:
        self.__del__()
        return False


def save_monitor_output(monitor: Monitor, path: str) -> None:
    # Get the live renderable and save it to a file
    saving_console = Console(record=True)
    saving_console.print(monitor.live.renderable)
    saving_console.save_html(path)


def check_monitor_output(monitor: Monitor, test_name: str) -> None:
    save_monitor_output(monitor, os.path.join(OUTPUTS, f"{test_name}.html"))
    assert filecmp.cmp(
        os.path.join(FIXTURES, f"{test_name}.html"),
        os.path.join(OUTPUTS, f"{test_name}.html"),
    )
