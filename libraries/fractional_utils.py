# This file contains all the functions used by fractional converter functions
# in 'fractional_converters.py' file.

def convert_fractional_part_from_decimal(fractional, end_base, stop):
    try:
        result = ""
        fractional = float("0." + fractional)
        iterations = 0

        if fractional == 0:
            return '0'

        while fractional != 0 \
              and iterations < stop:
            
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

    
def convert_fractional_part_to_decimal(fractional, start_base):
    try:
        result = 0.0

        for i in range(len(fractional)):
            result += int(fractional[i], start_base)*(start_base**(-(i+1)))
        
        return str(result)[2:]
    except:
        raise ValueError
