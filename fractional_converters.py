# This file contains all the converter functions for fractional numbers used by
# the main program.

from libraries.fractional_utils import *
from libraries.IEEE754_utils import *


# This list defines all the exportable functions to other files.
__all__ = [
    "convert_fractional_decimal_to_twos_complement",
    "convert_fractional_twos_complement_to_decimal",
    "convert_fractional_decimal_to_hexadecimal",
    "convert_fractional_hexadecimal_to_decimal",
    "convert_decimal_to_IEEE754",
    "convert_IEEE754_to_decimal",
]


def convert_fractional_decimal_to_twos_complement(number):
    try:
        parts = []

        if '.' in number:
            parts = number.split('.')
        else:
            parts = [number, ""]

        integer_part = convert_decimal_to_twos_complement(parts[0])
        fractional_part = convert_fractional_part_from_decimal(parts[1], 2)
        
        return integer_part + '.' + fractional_part
    except:
        raise ValueError


def convert_fractional_twos_complement_to_decimal(number):
    try:
        parts = []

        if '.' in number:
            parts = number.split('.')
        else:
            parts = [number, ""]
        
        integer_part = str(convert_twos_complement_to_decimal(parts[0]))
        b = convert_fractional_part_to_decimal(parts[1], 2)
        
        return integer_part + '.' + b
    except:
        raise ValueError


def convert_fractional_decimal_to_hexadecimal(number):
    try:
        parts = []

        if '.' in number:
            parts = number.split('.')
        else:
            parts = [number, ""]

        integer_part = convert_decimal_to_hexadecimal(parts[0])
        fractional_part = convert_fractional_part_from_decimal(parts[1], 16, 10)
        
        return integer_part + '.' + fractional_part
    except:
        raise ValueError


def convert_fractional_hexadecimal_to_decimal(number):
    try:
        parts = []

        if '.' in number:
            parts = number.split('.')
        else:
            parts = [number, ""]

        integer_part = str(convert_hexadecimal_to_decimal(parts[0]))
        fractional_part = convert_fractional_part_to_decimal(parts[1], 16)
        
        return integer_part + '.' + fractional_part
    except:
        raise ValueError


def convert_decimal_to_IEEE754(precision, number) -> str:
    # Define useful variables
    match precision:
        case "half":
            bias = 15
            exp_digits = 5
            mant_digits = 10
        case "single":
            bias = 127
            exp_digits = 8
            mant_digits = 23
        case "double":
            bias = 1023
            exp_digits = 11
            mant_digits = 52
    
    # Check special cases
    match number:
        case "0":
            return "0" + " | " + "0" * exp_digits + " | " + "0" * mant_digits
        case "NaN":
            return "1" + " | " + "1" * exp_digits + " | " + "1" * mant_digits
        case "+infinity":
            return "0" + " | " + "1" * exp_digits + " | " + "0" * mant_digits
        case "-infinity":
            return "1" + " | " + "1" * exp_digits + " | " + "0" * mant_digits

    
    if number[0] in ['+', '-']:
        if number[0] == '+':
            sign = '0'
        else:
            sign = '1'

        number = number[1:]
    else:
        sign = '0'   

    parts = []

    if '.' in number:
        parts = number.split('.')
    else:
        parts = [number, ""]

    integer_part = bin(int(parts[0]))[2:]
    fractional_part = convert_fractional_part_from_decimal(parts[1], 2, bias*2)
    mantissa = integer_part + fractional_part

    higher_bound = bias
    lower_bound = -bias + 1
    lower_denormal_bound = -bias + 1 - mant_digits

    if integer_part == '0':
        if '1' not in fractional_part:
            raise UnderflowError
        
        exponent = -(mantissa.index('1'))

        if exponent < lower_bound:
            if exponent < lower_denormal_bound:
                raise UnderflowError
            
            start = bias
            mantissa = mantissa[start:start+mant_digits+1]
            exponent = -bias

            exponent, mantissa = round_IEEE754_mantissa(exponent, mantissa, mant_digits)
            return normalize_IEEE754_result(sign, exponent, mantissa, exp_digits, mant_digits, bias)
        
        start = mantissa.index('1') + 1
        mantissa = mantissa[start:start+mant_digits+1]
        
        exponent, mantissa = round_IEEE754_mantissa(exponent, mantissa, mant_digits)
        return normalize_IEEE754_result(sign, exponent, mantissa, exp_digits, mant_digits, bias)

    exponent = len(integer_part) - 1
    start = 1
    mantissa = mantissa[start:start+mant_digits+1]

    exponent, mantissa = round_IEEE754_mantissa(exponent, mantissa, mant_digits)

    if exponent > higher_bound:
        raise OverflowError

    return normalize_IEEE754_result(sign, exponent, mantissa, exp_digits, mant_digits, bias)


def convert_IEEE754_to_decimal(sign, exponent, mantissa):
    if '1' not in exponent:
        if '1' not in mantissa:
            return '0'
        
        mantissa = '0' + mantissa
    elif '0' not in exponent:
        if '1' in mantissa:
            return "-infinity" if int(sign) else "+infinity"
        else:
            return "NaN"
    else:
        mantissa = '1' + mantissa

    exponent = int(exponent, 2) - (2 ** (len(exponent) - 1) - 1)
    actual_value = 0
    index = 0
    for digit in mantissa:
        actual_value += int(digit) * 2 ** (exponent - index)
        index += 1
    
    return str(-actual_value) if int(sign) else str(actual_value)
