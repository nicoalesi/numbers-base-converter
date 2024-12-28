# This file contains some useful functions used by IEEE754 converter functions
# in 'fractional_converters.py' file.

from libraries.exceptions import MantissaError, PrecisionError, SignError
from libraries.message_printers import print_from_IEEE754_information
from libraries.message_printers import print_to_IEEE754_information


# This list defines all the exportable functions to other files.
__all__ = [
    "get_to_IEEE754_inputs",
    "get_from_IEEE754_inputs",
    "normalize_IEEE754_result",
    "round_IEEE754_mantissa"
]


# This function gets all the necessary information for decimal-to-IEEE754
# conversion.
def get_to_IEEE754_inputs() -> tuple:
    # Print usage.
    print_to_IEEE754_information()

    # Check if the chosen precision is supported by the program.
    precision = input("Precision: ")
    if precision not in ["half", "single", "double"]:
        raise PrecisionError
    
    number = input("Number to convert: ")

    return precision, number


# This function gets all the necessary information for IEE754-to-decimal
# conversion.
def get_from_IEEE754_inputs() -> tuple:
    # Print usage.
    print_from_IEEE754_information()

    # This dictionary contains all exponents' allowed lengths with their
    # corresponding maximum mantissas' lengths.
    lengths_allowed = {
        5: 10,
        8: 23,
        11: 52,
    }

    # The sign must be '0' (+) or '1' (-), otherwise an exception is raised.
    sign = input("Sign: ")
    if sign not in ['0', '1']:
        raise SignError

    # The exponent must be as long as one of the specified lengths because
    # the precision of the IEEE754 is calculated by its length.
    exponent = input("Exponent: ")
    exp_length = len(exponent)
    if exp_length not in lengths_allowed:
        raise PrecisionError
    
    # The mantissa must be shorter than the maximum length of its specific
    # precision, otherwise an exception is raised.
    mantissa = input("Mantissa: ")
    mant_length = len(mantissa)
    if mant_length > lengths_allowed[exp_length]:
        raise MantissaError

    return sign, exponent, mantissa


# This functions creates the formatted final string to print.
def normalize_IEEE754_result(sign, exponent, mantissa, \
      exp_length, mant_length, bias) -> str:
    
    # Convert the exponent to binary and cut the '0b' prefix.
    exponent = bin(exponent + bias)[2:]

    # If the exponent is too short fill it with 0s.
    if len(exponent) < exp_length:
        exponent = '0'*(exp_length-len(exponent)) + exponent
    
    # If the mantissa is too short fill it with 0s.
    if len(mantissa) < mant_length:
        mantissa = '0'*(mant_length-len(mantissa)) + mantissa

    return sign + " | " + exponent + " | " + mantissa


# This function rounds the mantissa to the nearest representable value.
def round_IEEE754_mantissa(exponent, mantissa, length) -> tuple:

    # If the mantissa is composed by all 1s it becomes all 0s and the
    # exponent is incremented
    if mantissa == '1' * (length+1):
        exponent += 1
        mantissa = '0' * length
        return exponent, mantissa
    
    # If the first digit after the shown mantissa is '1' then round it
    # by adding one, otherwise do nothing.
    if mantissa[-1] == '1':
        mantissa = bin(int(mantissa, 2) + 1)[2:]
    
    return exponent, mantissa[:-1]
