# Write a function to calculate
# the area of a circle with radius r
# test it with pytest
# step 1: write the stub

import math
import pytest
def areaOfCircle(radius):
    '''returns the area of a circle'''
    result = math.pi * radius ** 2
    return result

# step2: write the test cases
def test_1():
    assert areaOfCircle(1) == math.pi

def test_2():
    assert areaOfCircle(2) == 4*math.pi

def test_3():
    assert math.sqrt(2)*math.sqrt(2) == pytest.approx(2)

# Step 3: Run pytest from terminal using the command
# python3 -m pytest areaOfCircle.py

# Step 4: Look at the output of pytest and identify the
# the test cases that are failing. Read the error message
# to understand why they are failing
