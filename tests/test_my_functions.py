import time
import pytest
import Source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_concatenate_strings():
    result = my_functions.add("I like ", "burgers")
    assert result == "I like burgers"

def test_divide():
    result = my_functions.divide(4, 2)
    # assert does a conditional check, if the expression results in true the code is allowed to continue running
    # ans we get a passed test, because it reaches the end of its execution context. If it results in false assert
    # cuts the thread and raises an assertion error class.
    assert result == 2

# Even though we're testing the same divide function as above we should still create a separate unit test because
# we're testing for a separate edge case/piece of logic. We want our unit tests narrow down errors and be as
# specific as possible, so we know exactly where they're coming from.
def test_divide_by_zero():
    # To test for Exceptions use the following syntax:
    with pytest.raises(ZeroDivisionError):
        result = my_functions.divide(4, 0)

# Marks the test with a slow tag, to specifically run tests with a certain mark use -m mark in the terminal
@pytest.mark.slow
def test_very_slow():
    # Setups a function that stops execution for 5 seconds
    time.sleep(5)
    result = my_functions.add(1, 4)
    assert result == 5

@pytest.mark.skip(reason="this feature is broken at the moment.")
def test_dumb():
    result = my_functions.add(1, 4)
    assert result == 5

# We know test will fail and dont want to fix it for some reason.
@pytest.mark.xfail(reason="We know we cant divide by zero.")
def test_divide_by_zero():
    my_functions.divide(4, 2)

