import pytest
import math
import Source.shapes as shapes

# This is how you test classes
class TestCircle:

    # When writing class tests, we need to have two methods. One that writes setup code before each test method
    # Then one that tears it down at the end of each test
    def setup_method(self, method):
        print(f"Setting up {method}")
        # For each method test instantiate the Circle class.
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2