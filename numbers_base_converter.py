class PrecisionError(Exception):
    ...

class SignError(Exception):
    ...

class OverflowError(Exception):
    ...

class UnderflowError(Exception):
    ...

def convert_decimal_to_binary(number):
    try:
        if number[0] == '-':
            raise ValueError

        result = bin(int(number))
        return result
    except:
        raise ValueError


def convert_binary_to_decimal(number):
    try:
        if number[0] == '-':
            raise ValueError

        result = int(number, 2)
        return result
    except:
        raise ValueError


def convert_decimal_to_hexadecimal(number):
    try:
        if number[0] == '-':
            raise ValueError

        result = hex(int(number))
        return result
    except:
        raise ValueError


def convert_hexadecimal_to_decimal(number):
    try:
        if number[0] == '-':
            raise ValueError

        result = int(number, 16)
        return result
    except:
        raise ValueError


def convert_hexadecimal_to_binary(number):
    try:
        result = convert_hexadecimal_to_decimal(number)
        result = convert_decimal_to_binary(str(result))
        return result
    except:
        raise ValueError


def convert_binary_to_hexadecimal(number):
    try:
        result = convert_binary_to_decimal(number)
        result = convert_decimal_to_hexadecimal(str(result))
        return result
    except:
        raise ValueError


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


def get_to_IEEE754_inputs():
    print_to_IEEE754_information()

    precision = input("Precision: ")
    if precision not in ["half", "single", "double"]:
        raise PrecisionError
    
    number = input("Number to convert: ")

    return precision, number


def get_from_IEEE754_inputs():
    print_from_IEEE754_information()

    sign = input("Sign: ")
    if sign not in ['0', '1']:
        raise SignError

    exponent = input("Exponent: ")
    if len(exponent) not in [5, 8, 11]:
        raise ExponentError


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

    if integer_part == '0' \
          and'1' not in fractional_part:
        raise UnderflowError

    if integer_part == '0':
        exponent = -(fractional_part.index('1') + 1)
    else:
        exponent = len(integer_part) - 1
    
    mantissa = integer_part[1:] + fractional_part

    higher_bound = bias
    lower_bound = -bias + 1
    lower_denormal_bound = -bias + 1 - mant_digits

    if exponent > higher_bound:
        raise OverflowError

    if exponent < lower_bound:
        if exponent < lower_denormal_bound:
            raise UnderflowError
        else:
            space = -exponent - bias
            exponent = lower_bound - 1
            mantissa = '0' * space + mantissa[(-lower_bound + space):-lower_bound+mant_digits+1]
        
    if len(mantissa) > mant_digits:
        if mantissa[mant_digits] == '1':
            if mantissa[:mant_digits] == ('1' * mant_digits):
                exponent += 1
                mantissa = '0' * mant_digits
            else:
                mantissa = bin(int(mantissa[:mant_digits], 2) + 1)[2:]
        else:
            mantissa = mantissa[:mant_digits]
            
    exponent = bin(exponent + bias)[2:]

    if len(exponent) < exp_digits:
        exponent = '0'*(exp_digits-len(exponent)) + exponent
    
    if len(mantissa) < mant_digits:
        mantissa = '0'*(mant_digits-len(mantissa)) + mantissa

    return sign + " | " + exponent + " | " + mantissa


def convert_IEEE754_to_decimal(number):
    ...


def print_to_IEEE754_information():
    print()

    print("+------------------------ IEEE754 USAGE -------------------------+")
    print("|                                                                |")
    print("|  Choose one of the following options:                          |")
    print("|                                                                |")
    print("|   - half                             (Half precision: 1-5-10)  |")
    print("|   - single                         (Single precision: 1-8-23)  |")
    print("|   - double                        (Double precision: 1-11-52)  |")
    print("|                                                                |")
    print("+----------------------------------------------------------------+")


def print_from_IEEE754_information():
    print()

    print("+------------------------ IEEE754 USAGE -------------------------+")
    print("|                                                                |")
    print("|  Half, single and double precision formats are allowed.        |")
    print("|  Remark: in IEEE754 sign is expressed as either 0 or 1.        |")
    print("|  Note: the format chosen will be determined by the exponent's  |")
    print("|        length, make sure to insert 5, 8 or 11 digits.          |")
    print("|                                                                |")
    print("+----------------------------------------------------------------+")


def print_information():
    print()

    print("+------------------------- INFORMATION --------------------------+")
    print("|                                                                |")
    print("|  Authors:                                                      |")
    print("|   Nicolo Alesi                                                 |")
    print("|   Enes Ozdemir                                                 |")
    print("|   Federico Alcantara                                           |")
    print("|                                                                |")
    print("|  License: MIT License                                          |")
    print("|                                                                |")
    print("+----------------------------------------------------------------+")


def print_instructions():
    print()

    print("+---------------------------- MODES -----------------------------+")
    print("|                                                                |")
    print("|  The following modes are available:                            |")
    print("|                                                                |")
    print("|  Unsigned numbers:                                             |")
    print("|   [1] Decimal > Binary          [2] Binary > Decimal           |")
    print("|   [3] Decimal > Hexadecimal     [4] Hexadecimal > Decimal      |")
    print("|   [5] Hexadecimal > Binary      [6] Binary > Hexadecimal       |")
    print("|                                                                |")
    print("|  Signed numbers:                                               |")
    print("|   [7] Decimal > S/Magnitude     [8] S/Magnitude > Decimal      |")
    print("|   [9] Decimal > 2's Complement  [10] 2's Complement > Decimal  |")
    print("|                                                                |")
    print("|  Fractional numbers:                                           |")
    print("|   [11] Decimal > 2's Complement               (Signed)         |")
    print("|   [12] 2's Complement > Decimal               (Signed)         |")
    print("|                                                                |")
    print("|   [13] Decimal > Hexadecimal                  (Unsigned)       |")
    print("|   [14] Hexadecimal > Decimal                  (Unsigned)       |")
    print("|                                                                |")
    print("|   [15] Decimal > IEEE754     (Half, Single, Double precision)  |")
    print("|   [16] IEEE754 > Decimal     (Half, Single, Double precision)  |")
    print("|                                                                |")
    print("+----------------------------------------------------------------+")
    

def print_header():
    print()    

    print("+----------------------- NUMBER CONVERTER -----------------------+")
    print("|                                                                |")
    print("|  Use this program to convert numbers                           |")
    print("|                                                                |")
    print("|  Commands:                                                     |")
    print("|   /convert              - Start the converter                  |")
    print("|   /help                 - Print this message again             |")
    print("|   /information          - Print useful information             |")
    print("|   /exit                 - Close this program                   |")
    print("|                                                                |")
    print("+----------------------------------------------------------------+")


def convert():
    conversion_mode = input("Convertion type: ")

    try:
        match conversion_mode:
            case '1':
                num = input("Number to convert: ")
                result = convert_decimal_to_binary(num)
            case '2':
                num = input("Number to convert: ")
                result = convert_binary_to_decimal(num)
            case '3':
                num = input("Number to convert: ")
                result = convert_decimal_to_hexadecimal(num)
            case '4':
                num = input("Number to convert: ")
                result = convert_hexadecimal_to_decimal(num)
            case '5':
                num = input("Number to convert: ")
                result = convert_hexadecimal_to_binary(num)
            case '6':
                num = input("Number to convert: ")
                result = convert_binary_to_hexadecimal(num)
            case '7':
                num = input("Number to convert: ")
                result = convert_decimal_to_sign_magnitude(num)
            case '8':
                num = input("Number to convert: ")
                result = convert_sign_magnitude_to_decimal(num)
            case '9':
                num = input("Number to convert: ")
                result = convert_decimal_to_twos_complement(num)
            case '10':
                num = input("Number to convert: ")
                result = convert_twos_complement_to_decimal(num)
            case '11':
                num = input("Number to convert: ")
                result = convert_fractional_decimal_to_twos_complement(num)
            case '12':
                num = input("Number to convert: ")
                result = convert_fractional_twos_complement_to_decimal(num)
            case '13':
                num = input("Number to convert: ")
                result = convert_fractional_decimal_to_hexadecimal(num)
            case '14':
                num = input("Number to convert: ")
                result = convert_fractional_hexadecimal_to_decimal(num)
            case '15':
                num, prec = get_to_IEEE754_inputs()
                result = convert_decimal_to_IEEE754(num, prec)
            case '16':
                sign, exp, mant = get_from_IEEE754_inputs()
                result = convert_IEEE754_to_decimal()
            case _:
                print("Mode not valid.")
                return
            
        if result != None:
            print("Result:", result)
    except PrecisionError:
        print("Precision not supported.")
    except UnderflowError:
        print("Underflow error.")



if __name__ == "__main__":
    print_header()

    while True:
        command = input("Command: ")

        match command:
            case "/convert":
                print_instructions()
                convert()
            case "/help":
                print_header()
            case "/information":
                print_information()
            case "/exit":
                break
            case _:
                print("Command not found.")
