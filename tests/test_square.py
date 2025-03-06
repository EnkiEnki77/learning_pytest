import pytest
import Source.shapes as shapes


# If we want to test for multiple different inputs, instead of writing a separate test for each input we
# write a single test, and then parameterize the inputs. So that the single test is run for each input.
# We first define the parameters that will be used in a single string.
# Next we define a list of tuples, where each tuple will be an individual test instance. And the values of
# the tuples are the arguments passed to the params
# @pytest.mark.parametrize("side_length, expected_area", [(5, 25), (6, 36), (7, 49)])
# # We now need to pass the params from our mark into the test function. my_square is a global fixture that
# # instantiates the Square class.
@pytest.mark.parametrize("my_square, expected_area", [(5, 25), (6, 36), (7,49)], indirect=["my_square"])
def test_multiple_square_areas(my_square, expected_area):
    assert my_square.area() == expected_area

# When you wish to pass a parameter as an argument to a fixture youre using in a test you can utilize indirect
# parametrization. This stores the value in the param property of a request object, and passes the request object
# to the fixture as an argument.
@pytest.mark.parametrize("my_square, expected_perimeter", [(5, 20), (6, 24), (7, 28)], indirect=["my_square"])
def test_perimeter_of_square(my_square, expected_perimeter):
    assert my_square.perimeter() == expected_perimeter

# @pytest.mark.parametrize("fixture_test", [True, False], indirect=["fixture_test"])
# def test_one(fixture_test):
#     assert fixture_test.do_this()
