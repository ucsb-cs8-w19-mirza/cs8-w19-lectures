# Write functions
# while also testing them

#import pytest

# Write a stub function
def dbl(x):
    #Empty shell for the code
    return 2*x

# Test cases
# Each case tests dbl
# using a specific set of inputs
# Each function should begin
# with test_
def test_case_1():
    #Check if the expected return value
    # is the same as the actual return value
    assert 0 == dbl(0)


def test_case_2():
    #Check if the expected return value
    # is the same as the actual return value
    assert 2 == dbl(1)

def test_case_3():
    assert "appleapple" == dbl("apple")
