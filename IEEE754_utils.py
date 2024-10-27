# This file contains some useful functions used by IEEE754 converter functions
# in 'fractional_converters.py' file.

def get_to_IEEE754_inputs():
    print_to_IEEE754_information()

    precision = input("Precision: ")
    if precision not in ["half", "single", "double"]:
        raise PrecisionError
    
    number = input("Number to convert: ")

    return precision, number


def get_from_IEEE754_inputs():
    print_from_IEEE754_information()

    lengths_allowed = {
        5: 10,
        8: 23,
        11: 52,
    }

    sign = input("Sign: ")
    if sign not in ['0', '1']:
        raise SignError

    exponent = input("Exponent: ")
    exp_length = len(exponent)
    if exp_length not in lengths_allowed:
        raise PrecisionError
    
    mantissa = input("Mantissa: ")
    mant_length = len(mantissa)
    if mant_length > lengths_allowed[exp_length]:
        raise MantissaError

    return sign, exponent, mantissa


def normalize_IEEE754_result(sign, exponent, mantissa, exp_length, mant_length, bias):
    exponent = bin(exponent + bias)[2:]

    if len(exponent) < exp_length:
        exponent = '0'*(exp_length-len(exponent)) + exponent
    
    if len(mantissa) < mant_length:
        mantissa = '0'*(mant_length-len(mantissa)) + mantissa

    return sign + " | " + exponent + " | " + mantissa


def round_IEEE754_mantissa(exponent, mantissa, length):

    if mantissa == '1' * (length+1):
        exponent += 1
        mantissa = '0' * length
        return exponent, mantissa
    
    if mantissa[-1] == '1':
        mantissa = bin(int(mantissa, 2) + 1)[2:]
    
    return exponent, mantissa[:-1]
