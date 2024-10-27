# This file contains all the converter functions for signed numbers used by
# the main program.

from libraries.unsigned_converters import convert_decimal_to_binary
from libraries.unsigned_converters import convert_binary_to_decimal


# This list defines all the exportable functions to other files.
__all__ = [
    "convert_decimal_to_sign_magnitude",
    "convert_sign_magnitude_to_decimal",
    "convert_decimal_to_twos_complement",
    "convert_twos_complement_to_decimal",
    ]

def convert_decimal_to_sign_magnitude(number):
    try:
        if number[0] in ['-', '+']:
            result = convert_decimal_to_binary(number[1:])

            if number[0] == '+':
                return "0b" + "0" + result[2:]
            else:
                return "0b" + "1" + result[2:]
        else:
            result = convert_decimal_to_binary(number)
            return "0b" + "0" + result[2:]
    except:
        raise ValueError


def convert_sign_magnitude_to_decimal(number):
    try:
        if number[:2] == '0b':
            if number[2] not in ['0', '1']:
                raise ValueError
            
            result = convert_binary_to_decimal(number[3:])

            if number[2] == '0':
                return result
            else:
                return -result
        else:
            if number[0] not in ['0', '1']:
                raise ValueError

            result = convert_binary_to_decimal(number[1:])

            if number[0] == '0':
                return result
            else:
                return -result
    except:
        raise ValueError


def convert_decimal_to_twos_complement(number):
    try:
        value = int(number)

        if value < 0:
            n_bits = value.bit_length()
            mask = (1 << (n_bits + 1)) - 1
            return bin(value & mask)
        else:
            return '0b' + '0' + bin(value)[2:]
    except:
        raise ValueError


def convert_twos_complement_to_decimal(number):
    try:
        if number[:2] == '0b':
            if number[2] not in ['0', '1']:
                raise ValueError

            result = int(number[2:], 2)

            if number[2] == '0':
                return result
            else:
                n_bits = result.bit_length()
                mask = (1 << n_bits) - 1
                result = int(bin(result ^ mask), 2) + 1
                return -result
        else:
            if number[0] not in ['0', '1']:
                raise ValueError

            result = int(number[1:], 2)

            if number[0] == '0':
                return result
            else:
                n_bits = result.bit_length()
                mask = (1 << n_bits) - 1
                result = int(bin(result ^ mask), 2) + 1
                return -result
    except:
        raise ValueError
