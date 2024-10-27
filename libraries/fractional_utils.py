# This file contains all the functions used by fractional converter functions
# in 'fractional_converters.py' file.

# This function converts the fractional part of a number from its decimal base
# to another base.
def convert_fractional_part_from_decimal(fractional: str, \
      end_base: int, stop: int) -> str:
    try:
        # The fractional part is converted to float to be able to perform
        # operations. 'result' and 'iterationes' variable are initialized.
        result = ""
        fractional = float("0." + fractional)
        iterations = 0

        # If the number is zero just return zero.
        if fractional == 0:
            return '0'

        # The procedure of conversion keeps going until the fractional part
        # becomes 0 or the limit of iterations is reached.
        while fractional != 0 \
              and iterations < stop:
            
            # Every iteration the fractional number is multiplied by
            # the base and if the result is greater than one, the
            # integer part is appended to the string and subtracted to
            # the fractional number.
            # If the result is less than 1, a '0' is appended to the string.
            fractional = fractional * end_base
            if fractional >= 1:
                excess = int(fractional)
                fractional -= excess
                result += hex(excess)[2]
            else:
                result += '0'
            
            iterations += 1

        return result
    except:
        raise ValueError

    
# This function converts the fractional part of a number from its starting base
# to decimal base.
def convert_fractional_part_to_decimal(fractional: str, start_base: int) -> str:
    try:
        # Initialize result to be able to add values to it.
        result = 0.0

        # Every digit is multiplied by the starting base to the power of
        # the opposite of the current position and added to the result.
        # Example:
        #   1 in 3rd position -> 1 * b**(-3)
        for i in range(len(fractional)):
            result += int(fractional[i], start_base)*(start_base**(-(i+1)))
        
        return str(result)[2:]
    except:
        raise ValueError
