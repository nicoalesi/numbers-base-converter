# This file contains all the converter functions for fractional numbers used by
# the main program.

from libraries.exceptions import OverflowError, UnderflowError
from libraries.fractional_utils import *
from libraries.IEEE754_utils import *
from libraries.signed_converters import convert_decimal_to_twos_complement
from libraries.signed_converters import convert_twos_complement_to_decimal
from libraries.unsigned_converters import convert_decimal_to_hexadecimal
from libraries.unsigned_converters import convert_hexadecimal_to_decimal


# This list defines all the exportable functions to other files.
__all__ = [
    "convert_fractional_decimal_to_twos_complement",
    "convert_fractional_twos_complement_to_decimal",
    "convert_fractional_decimal_to_hexadecimal",
    "convert_fractional_hexadecimal_to_decimal",
    "convert_decimal_to_IEEE754",
    "convert_IEEE754_to_decimal",
]


# This function converts fractional decimal numbers to two's complement
# numbers.
def convert_fractional_decimal_to_twos_complement(number: str) -> str:
    try:
        # This list stores both the integer and fractional part of the number.
        parts = []

        # Break the number in two parts splitting with the '.' character.
        # If there is no '.' it is an integer number and the fractional
        # part is empty.
        if '.' in number:
            parts = number.split('.')
        else:
            parts = [number, ""]

        # Convert the number using already existing functions.
        integer_part = convert_decimal_to_twos_complement(parts[0])
        fractional_part = convert_fractional_part_from_decimal(parts[1], 2, 10)
        
        # Return the formatted result.
        return integer_part + '.' + fractional_part
    except:
        raise ValueError


# This function converts fractional two's complement numbers to decimal numbers.
def convert_fractional_twos_complement_to_decimal(number: str) -> str:
    try:
        # This list stores both the integer and fractional part of the number.
        parts = []

        # Break the number in two parts splitting with the '.' character.
        # If there is no '.' it is an integer number and the fractional
        # part is empty.
        if '.' in number:
            parts = number.split('.')
        else:
            parts = [number, ""]
        
        # Convert the number using already existing functions.
        integer_part = str(convert_twos_complement_to_decimal(parts[0]))
        fractional_part = convert_fractional_part_to_decimal(parts[1], 2)
        
        # Return the formatted result.
        return integer_part + '.' + fractional_part
    except:
        raise ValueError


# This function converts fractional decimal numbers to hexadecimal numbers.
def convert_fractional_decimal_to_hexadecimal(number: str) -> str:
    try:
        # This list stores both the integer and fractional part of the number.
        parts = []

        # Break the number in two parts splitting with the '.' character.
        # If there is no '.' it is an integer number and the fractional
        # part is empty.
        if '.' in number:
            parts = number.split('.')
        else:
            parts = [number, ""]

        # Convert the number using already existing functions.
        integer_part = convert_decimal_to_hexadecimal(parts[0])
        fractional_part = convert_fractional_part_from_decimal(parts[1], 16, 10)
        
        # Return the formatted result.
        return integer_part + '.' + fractional_part
    except:
        raise ValueError


# This function converts fractional hexadecimal numbers to decimal numbers.
def convert_fractional_hexadecimal_to_decimal(number: str) -> str:
    try:
        # This list stores both the integer and fractional part of the number.
        parts = []

        # Break the number in two parts splitting with the '.' character.
        # If there is no '.' it is an integer number and the fractional
        # part is empty.
        if '.' in number:
            parts = number.split('.')
        else:
            parts = [number, ""]

        # Convert the number using already existing functions.
        integer_part = str(convert_hexadecimal_to_decimal(parts[0]))
        fractional_part = convert_fractional_part_to_decimal(parts[1], 16)
        
        # Return the formatted result.
        return integer_part + '.' + fractional_part
    except:
        raise ValueError


# This function converts decimal numbers to floating point IEEE754 numbers.
def convert_decimal_to_IEEE754(precision: str, number: str) -> str:
    try:
        # Define constants fro current precision.
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
        
        # Check special cases.
        match number:
            case "0":
                return "0" + " | " + "0" * exp_digits + " | " + "0" * mant_digits
            case "NaN":
                return "1" + " | " + "1" * exp_digits + " | " + "1" * mant_digits
            case "+infinity":
                return "0" + " | " + "1" * exp_digits + " | " + "0" * mant_digits
            case "-infinity":
                return "1" + " | " + "1" * exp_digits + " | " + "0" * mant_digits

        # Update the 'sign' variable.
        if number[0] in ['+', '-']:
            if number[0] == '+':
                sign = '0'
            else:
                sign = '1'

            number = number[1:]
        else:
            sign = '0'   

        # This list stores both the integer and fractional part of the number.
        parts = []

        # Break the number in two parts splitting with the '.' character.
        # If there is no '.' it is an integer number and the fractional
        # part is empty.
        if '.' in number:
            parts = number.split('.')
        else:
            parts = [number, ""]

        # Convert the number using already existing functions.
        integer_part = bin(int(parts[0]))[2:]
        fractional_part = convert_fractional_part_from_decimal(parts[1], 2, bias*2)
        # Merge them to obtain the mantissa
        mantissa = integer_part + fractional_part

        # Define boundaries.
        higher_bound = bias
        lower_bound = -bias + 1
        lower_denormal_bound = -bias - mant_digits

        if integer_part == '0':
            # If there are no 1s in the fractional part the number is too small
            # to be represented.
            if '1' not in fractional_part:
                raise UnderflowError
            
            # The exponent is obtained by taking the opposite position of the
            # first occurrence of '1'.
            exponent = -(mantissa.index('1'))

            # If the exponent is less than 'lower_bound' can be either a denormal
            # or an Underflow.
            if exponent < lower_bound:
                # If the exponent is smaller than the lower denormal numer it is
                # too small to be represented.
                if exponent < lower_denormal_bound:
                    raise UnderflowError
                
                # It is a denormal.
                # Define and update variables to the current case.
                start = bias
                mantissa = mantissa[start:start+mant_digits+1]
                exponent = -bias

                # Round the result, normalize it and return it.
                exponent, mantissa = round_IEEE754_mantissa(exponent, mantissa, mant_digits)
                return normalize_IEEE754_result(sign, exponent, mantissa, exp_digits, mant_digits, bias)
            
            # The number is only fractional (no integer part) but big enough to
            # be represented normally.
            # Define and update variables to the current case.
            start = mantissa.index('1') + 1
            mantissa = mantissa[start:start+mant_digits+1]
            
            # Round the result, normalize it and return it.
            exponent, mantissa = round_IEEE754_mantissa(exponent, mantissa, mant_digits)
            return normalize_IEEE754_result(sign, exponent, mantissa, exp_digits, mant_digits, bias)

        # The number is composed by both an integer part and fractional part.
        # The first digit is always one so to get the exponent it is necessary to
        # shift until the second digit, this means that the comma shifts of the 
        # length of the integer part minus one.
        exponent = len(integer_part) - 1
        start = 1
        mantissa = mantissa[start:start+mant_digits+1]

        # If the number of digits of the mantissa is lower than required
        # append zeros to the end until required length + 1.
        # Necessary for correct rounding.
        if len(mantissa) < mant_digits:
            mantissa += "0"*(mant_digits-len(mantissa)+1)

        # Round the result.
        exponent, mantissa = round_IEEE754_mantissa(exponent, mantissa, mant_digits)

        # Check if the result is too big to be represented.
        if exponent > higher_bound:
            raise OverflowError

        # Normalize and return the result.
        return normalize_IEEE754_result(sign, exponent, mantissa, exp_digits, mant_digits, bias)
    except ValueError:
        raise ValueError
    except OverflowError:
        raise OverflowError
    except UnderflowError:
        raise UnderflowError


# This function converts floating point IEEE754 numbers to decimal numbers.
def convert_IEEE754_to_decimal(sign: str, exponent: str, mantissa: str) -> int:
    try:
        if '1' not in exponent:
            # If '1' is neither in the exponent nor in the mantissa it is a special
            # case, the number is 0.
            if '1' not in mantissa:
                return '0'
            
            # If there is a '1' in the mantissa it is a denormal.
            mantissa = '0' + mantissa
        # If there are no 0s in the exponent it is a special case.
        elif '0' not in exponent:
            # If there is a '1' in the mantissa it is either '-infinity' or 
            # '+infinity' based off the sign. Otherwise it is 'NaN'.
            if '1' in mantissa:
                return "-infinity" if int(sign) else "+infinity"
            else:
                return "NaN"
        else:
            # In all other cases it is a normal number.
            mantissa = '1' + mantissa

        # The exponent is calculated subtracting the bias to it.
        bias = 2**(len(exponent) - 1) - 1
        exponent = int(exponent, 2) - bias

        # Define useful variables.
        actual_value = 0
        index = 0

        # Calculate the value iterating through the mantissa.
        for digit in mantissa:
            actual_value += int(digit) * 2 ** (exponent - index)
            index += 1
        
        # Return the result, positive or negative based on the sign.
        return -actual_value if int(sign) else actual_value
    except ValueError:
        raise ValueError
