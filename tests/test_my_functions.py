import pytest
import Source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

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

