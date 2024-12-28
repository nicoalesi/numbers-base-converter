# This file contains all the tests to ensure that edge cases work.
# If you want to run it make sure to install pytest and use
# the command 'pytest test.py'.

import pytest

from libraries.exceptions import *
from libraries.fractional_converters import convert_decimal_to_IEEE754


# This function tests edge cases between normal numbers representation
# and denormal numbers representation.
def test_normals_denormals_boundaries():
    assert convert_decimal_to_IEEE754(
        "single",
        "0.000000000000000000000000000000000000011754942"
    ) == "0 | 00000000 | 11111111111111111111111"
    
    assert convert_decimal_to_IEEE754(
        "single",
        "0.000000000000000000000000000000000000011754943"
    ) == "0 | 00000001 | 00000000000000000000000"


# This function tests denormal representation.
def test_denormals():
    assert convert_decimal_to_IEEE754(
        "single",
        "0.0000000000000000000000000000000000000000001"
    ) == "0 | 00000000 | 00000000000000001000111"
    
    assert convert_decimal_to_IEEE754(
        "single",
        "0.000000000000000000000000000000000000005139872"
    ) == "0 | 00000000 | 01101111111011111011111"


# This function tests edge cases regarding the smallest numbers
# representable and underflow errors.
def test_lower_boundaries():
    assert convert_decimal_to_IEEE754(
        "single",
        "0.00000000000000000000000000000000000000000000071064923"
    ) == "0 | 00000000 | 00000000000000000000001"
    
    with pytest.raises(UnderflowError):
        assert convert_decimal_to_IEEE754(
            "single",
            "0.00000000000000000000000000000000000000000000070064923"
        )


# This function tests edge cases regarding the largest numbers
# representable and overflow errors. 
def test_higher_boundaries():
    assert convert_decimal_to_IEEE754(
        "single",
        "340282350000000000000000000000000000000"
    ) == "0 | 11111110 | 11111111111111111111111"

    with pytest.raises(OverflowError):
        assert convert_decimal_to_IEEE754(
        "single",
        "340282357000000000000000000000000000000"
    )
