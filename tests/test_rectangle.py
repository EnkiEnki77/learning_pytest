import pytest
import Source.shapes as shapes

# In the below tests we're repeating ourselves creating an instance of Rectangle in each test. In class
# based tests we can initialize in the setup_method, but for function based tests we can use fixtures


# The fixture is then taken as an arg for your tests
def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 + 20) * 2

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle

