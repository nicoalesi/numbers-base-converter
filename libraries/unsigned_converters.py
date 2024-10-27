# This file contains all the converter functions for unsigned numbers used by
# the main program.

# This function converts decimal numbers to binary numbers.
def convert_decimal_to_binary(number: str) -> str:
    try:
        # If the number is negative raise an exception.
        if number[0] == '-':
            raise ValueError

        # Convert the number using built-in functions.
        result = bin(int(number))
        return result
    except:
        raise ValueError


# This function converts binary numbers to decimal numbers.
def convert_binary_to_decimal(number: str) -> int:
    try:
        # If the number is negative raise an exception.
        if number[0] == '-':
            raise ValueError

        # Convert the number using built-in functions.
        result = int(number, 2)
        return result
    except:
        raise ValueError


# This function converts decimal numbers to hexadecimal numbers.
def convert_decimal_to_hexadecimal(number: str) -> str:
    try:
        # If the number is negative raise an exception.
        if number[0] == '-':
            raise ValueError

        # Convert the number using built-in functions.
        result = hex(int(number))
        return result
    except:
        raise ValueError


# This function converts hexadecimal numbers to decimal numbers.
def convert_hexadecimal_to_decimal(number: str) -> int:
    try:
        # If the number is negative raise an exception.
        if number[0] == '-':
            raise ValueError

        # Convert the number using built-in functions.
        result = int(number, 16)
        return result
    except:
        raise ValueError


# This function converts hexadecimal numbers to binary numbers.
def convert_hexadecimal_to_binary(number: str) -> str:
    try:
        # Convert the number using previous functions.
        result = convert_hexadecimal_to_decimal(number)
        result = convert_decimal_to_binary(str(result))
        return result
    except:
        raise ValueError


# This function converts binary numbers to hexadecimal numbers.
def convert_binary_to_hexadecimal(number: str) -> str:
    try:
        result = convert_binary_to_decimal(number)
        result = convert_decimal_to_hexadecimal(str(result))
        return result
    except:
        raise ValueError
