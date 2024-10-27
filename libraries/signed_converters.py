# This file contains all the converter functions for signed numbers used by
# the main program.

from libraries.unsigned_converters import convert_binary_to_decimal
from libraries.unsigned_converters import convert_decimal_to_binary


# This list defines all the exportable functions to other files.
__all__ = [
    "convert_decimal_to_sign_magnitude",
    "convert_sign_magnitude_to_decimal",
    "convert_decimal_to_twos_complement",
    "convert_twos_complement_to_decimal",
    ]


# This function converts decimal numbers to sign/magnitude numbers.
def convert_decimal_to_sign_magnitude(number: str) -> str:
    try:
        # If there is a sign before the value of the number it is cut.
        if number[0] in ['-', '+']:
            result = convert_decimal_to_binary(number[1:])

            # Add sign digit before the value of the number.
            if number[0] == '+':
                return "0b" + "0" + result[2:]
            else:
                return "0b" + "1" + result[2:]
        else:
            # If there is no sign it is passed as it is.
            result = convert_decimal_to_binary(number)
            # The sign digit is 0 because no sign means positive number.
            return "0b" + "0" + result[2:]
    except:
        raise ValueError


# This function converts sign/magnitude numbers to decimal numbers.
def convert_sign_magnitude_to_decimal(number: str) -> int:
    try:
        # If the number starts with '0b' shift every operation by two.
        # Note: '0b' is the binary numbers' prefix.
        if number[:2] == '0b':
            # If the first digit is neither '0' nor '1' raise an exception.
            # This first digit is the sign digit.
            if number[2] not in ['0', '1']:
                raise ValueError
            
            # Convert the value part.
            result = convert_binary_to_decimal(number[3:])

            # Return a negative or positive integer based on the sign digit.
            if number[2] == '0':
                return result
            else:
                return -result
        else:
            # This code does has the same functions as the previous one but is
            # made for those numbers not starting with a prefix.

            # If the first digit is neither '0' nor '1' raise an exception.
            # This first digit is the sign digit.
            if number[0] not in ['0', '1']:
                raise ValueError

            # Convert only the value part.
            result = convert_binary_to_decimal(number[1:])

            # Return a negative or positive integer based on the sign digit.
            if number[0] == '0':
                return result
            else:
                return -result
    except:
        raise ValueError


# This function converts decimal numbers to two's complement numbers.
def convert_decimal_to_twos_complement(number: str) -> str:
    try:
        # Convert the number to integer to be able to use bitwise operations.
        value = int(number)

        # If the number is negative exploit its representation inside the
        # memory.
        if value < 0:
            # Calculate the number of bits used to represent the value of the
            # number.
            n_bits = value.bit_length()
            # Create a mask to perform a bitwise operation later.
            # This mask is composed by all 1s and it is as long as the number
            # of bits used to store the value of the number.
            mask = (1 << (n_bits + 1)) - 1
            # Return the binary form of the number obtained by performing a
            # bitwise 'and' between value and mask as follows:
            # Example:
            #   value  = 1001101
            #   mask   = 1111111
            #   result = 1001101
            # This represents a completely different integer number but we are
            # interested only in the binary representation in two's complement.
            return bin(value & mask)
        else:
            # If the number is positive simply add '0' at the start.
            return '0b' + '0' + bin(value)[2:]
    except:
        raise ValueError


# This function converts two's complement numbers to decimal numbers.
def convert_twos_complement_to_decimal(number: str) -> int:
    try:
        # If the number starts with '0b' shift every operation by two.
        # Note: '0b' is the binary numbers' prefix.
        if number[:2] == '0b':
            # If the first digit is neither '0' nor '1' raise an exception.
            # This first digit is the sign digit.
            if number[2] not in ['0', '1']:
                raise ValueError

            # Convert the number to integer cutting the prefix but not the
            # sign.
            result = int(number[2:], 2)

            # If the sign is '0' then the number is positive and the 
            # value is directly returned.
            if number[2] == '0':
                return result
            else:
                # Calculate the number of bits used to represent the value of
                # the number.
                n_bits = result.bit_length()
                # Create a mask to perform a bitwise operation later.
                # This mask is composed by all 1s and it is as long as the
                # number of bits used to store the value of the number.
                mask = (1 << n_bits) - 1
                # Return the integer, obtained from the binary number derived
                # from the bitwise 'xor' operation between the result and the
                # mask, plus one. This represents the manual procedure of 
                # flipping all digits and adding one to convert the number.
                # Example: 
                #   prev result = 10010111
                #   mask        = 11111111
                #   new result  = 01101000
                #   int(01101000) = 104 + 1 = 105
                result = int(bin(result ^ mask), 2) + 1
                # Return the opposite of the new result because it is a
                # negative number.
                return -result
        else:
            # If the first digit is neither '0' nor '1' raise an exception.
            # This first digit is the sign digit.
            if number[0] not in ['0', '1']:
                raise ValueError

            # Convert the number to integer cutting the sign.
            result = int(number[1:], 2)

            # Return instantly the number if it is positive.
            if number[0] == '0':
                return result
            else:
                # This part affects only negative numbers.
                # Calculate the number of bits used to represent the value of
                # the number.
                n_bits = result.bit_length()
                # Create a mask to perform a bitwise operation later.
                # This mask is composed by all 1s and it is as long as the
                # number of bits used to store the value of the number.
                mask = (1 << n_bits) - 1
                # Return the integer, obtained from the binary number derived
                # from the bitwise 'xor' operation between the result and the
                # mask, plus one. This represents the manual procedure of 
                # flipping all digits and adding one to convert the number.
                # Example: 
                #   prev result = 10010111
                #   mask        = 11111111
                #   new result  = 01101000
                #   int(01101000) = 104 + 1 = 105
                result = int(bin(result ^ mask), 2) + 1
                # Return the opposite of the new result because it is a
                # negative number.
                return -result
    except:
        raise ValueError
