# use this file to make fixtures global to all your tests
import pytest
import Source.shapes as shapes

# These defined fixtures can now be passed as arguments to any test in any test file.
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)