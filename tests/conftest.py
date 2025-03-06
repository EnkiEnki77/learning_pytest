# use this file to make fixtures global to all your tests
import pytest
import Source.shapes as shapes

# These defined fixtures can now be passed as arguments to any test in any test file.
@pytest.fixture
def my_rectangle():
    """Create a rectangle"""
    return shapes.Rectangle(10, 20)

@pytest.fixture
def weird_rectangle():
    """Create a weird rectangle"""
    return shapes.Rectangle(5, 6)

@pytest.fixture
# When you pass an argument to a fixture through indirect parametrization the argument is made the property
# of a request object. The request object is what is passed as the argument
def my_square(request):
    """Create a square"""
    # The value you were intending to pass to the fixture is stored in the param property of the request object
    print(f"fixture input is: {request.param}")
    return shapes.Square(request.param)

# class MyTest:
#     def __init__(self, x):
#         self.x = x
#
#     def do_this(self):
#         return self.x
#
# @pytest.fixture
# def fixture_test(request):
#     return MyTest(request.param)