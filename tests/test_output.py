from tests.utils import IndentedLoggerGetter, check_output, cleanup


def test_indented(cleanup):
    with IndentedLoggerGetter() as ilog:

        @ilog()
        def function_1():
            return function_2()

        @ilog()
        def function_2():
            return function_3()

        @ilog()
        def function_3():
            return 0

        function_1()
        check_output(ilog, "test_indented")


def test_not_indented(cleanup):
    with IndentedLoggerGetter() as ilog:

        @ilog()
        def function_1():
            return 0

        @ilog()
        def function_2():
            return 0

        @ilog()
        def function_3():
            return 0

        function_1()
        function_2()
        function_3()
        check_output(ilog, "test_not_indented")


def test_simple_loop(cleanup):
    with IndentedLoggerGetter() as ilog:

        @ilog()
        def function_1():
            for _ in ilog(range(2)):
                pass

        function_1()
        check_output(ilog, "test_simple_loop")


def test_complex_loop(cleanup):
    with IndentedLoggerGetter() as ilog:

        @ilog()
        def inner_function():
            return 0

        @ilog()
        def main_function():
            for _ in ilog(range(2)):
                for _ in ilog(range(2)):
                    inner_function()

        main_function()
        check_output(ilog, "test_complex_loop")


def test_names(cleanup):
    with IndentedLoggerGetter() as ilog:

        @ilog(name="function_1")
        def function_1():
            for _ in ilog(range(2), name="loop_1"):
                pass

        function_1()
        check_output(ilog, "test_names")


def test_leave(cleanup):
    with IndentedLoggerGetter() as ilog:

        @ilog(leave=False)
        def function_1():
            return function_2()

        @ilog()
        def function_2():
            return 0

        @ilog()
        def function_3():
            for _ in ilog(range(2), leave=False):
                pass

        function_1()
        function_2()
        function_3()
        check_output(ilog, "test_leave")


def test_context_manager(cleanup):
    with IndentedLoggerGetter() as ilog:

        @ilog()
        def function_1():
            return function_2()

        def function_2():
            with ilog():
                return 0

        function_1()
        check_output(ilog, "test_context_manager")


def test_class_method(cleanup):
    with IndentedLoggerGetter() as ilog:

        class MyClass:
            @ilog()
            def my_method(self):
                return 0

        my_class = MyClass()

        @ilog()
        def function_1():
            return my_class.my_method()

        function_1()
        check_output(ilog, "test_class_method")
