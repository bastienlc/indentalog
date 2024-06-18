from tests.utils import MonitorGetter, check_monitor_output, cleanup


def test_indented(cleanup):
    with MonitorGetter() as monitor:

        @monitor()
        def function_1():
            return function_2()

        @monitor()
        def function_2():
            return function_3()

        @monitor()
        def function_3():
            return 0

        function_1()
        check_monitor_output(monitor, "test_indented")


def test_not_indented(cleanup):
    with MonitorGetter() as monitor:

        @monitor()
        def function_1():
            return 0

        @monitor()
        def function_2():
            return 0

        @monitor()
        def function_3():
            return 0

        function_1()
        function_2()
        function_3()
        check_monitor_output(monitor, "test_not_indented")


def test_simple_loop(cleanup):
    with MonitorGetter() as monitor:

        @monitor()
        def function_1():
            for _ in monitor(range(2)):
                pass

        function_1()
        check_monitor_output(monitor, "test_simple_loop")


def test_complex_loop(cleanup):
    with MonitorGetter() as monitor:

        @monitor()
        def inner_function():
            return 0

        @monitor()
        def main_function():
            for _ in monitor(range(2)):
                for _ in monitor(range(2)):
                    inner_function()

        main_function()
        check_monitor_output(monitor, "test_complex_loop")
