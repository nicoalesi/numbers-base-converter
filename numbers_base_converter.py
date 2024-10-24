class PrecisionError(Exception):
    ...

class SignError(Exception):
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


def convert_fractional_part_from_decimal(fractional, end_base):
    try:
        result = ""
        fractional = float("0." + fractional)
        iterations = 0

        if fractional == 0:
            return '0'

        while fractional != 0 \
              and iterations < 10:
            
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
        fractional_part = convert_fractional_part_from_decimal(parts[1], 16)
        
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


def convert_IEEE754_to_decimal(number):
    ...

def add_one(a: str) -> str:
    '''
    add 1 to a binary number 

    a: binary number
    '''

    res = ''

    b =  '1'.zfill(len(a)) # binary number 1

    carry = '0' # carried bit during sum

    for i, j in zip(a[::-1], b[::-1]):
        if i == '1' and j == '1' and carry == '0':
            res += '0'

            carry = '1'
        elif i == '1' and j == '1' and carry == '1':
            res += '1'

            carry = '1'
        elif ((i == '1' and j == '0') or (i == '0' and j == '1')) and carry == '0':
            res += '1'
        elif ((i == '1' and j == '0') or (i == '0' and j == '1')) and carry == '1':
            res += '0'

            carry = '1'
        elif i == '0' and j == '0':
            res += carry

            carry = '0'

    res = res[::-1]

    return res
    
def dec_part_to_bin(x: int):
    ''''
    convert decimal part to binary (first method that doesn't work for very small numbers)

    x: decimal number 
    '''

    res = ''
    viewed = [] # list of numbers already seen, used to understand when there is a cycle 

    while x != 0 and x not in viewed:
        viewed.append(x)
    
        x *= 2

        if x < 1:
            res += '0'
        else:
            res += '1'

            x -= 1

    return res
    
def dec_part_to_bin_2(x: int, prec: int):
    ''''
    convert decimal part to binary (second method that work for very small numbers)

    x: decimal number
    '''

    res = ''

    close_x = 0 # number that has to be as close as possible to x
    count_ones = 0

    len_m = {
        16: 10,
        32: 23,
        64: 55
    }
    
    prec_m = len_m[prec] # precison of mantissa, for very small fractions like 0.000002341, until when calculate bits

    i = 1
    
    while count_ones < prec_m:
        power = pow(2, -i)

        if power + close_x < x:
            res += '1'

            close_x += power

            count_ones += 1
        elif power + close_x > x:
            res += '0'
        else:
            if i == 1:
                return '1'
            else:
                return res + '1'
    
        i += 1

    return res

def bit_ext(self, x: str, type: str):
    '''
    does a binary extension

    x: binary number
    type: s(igned) or u(nsigned)
    '''

    bit_to_ext = self.n - len(x) 

    pre = '1' * bit_to_ext if type == 's' else '0' * bit_to_ext

    x = pre + x

    return x

def convert_decimal_to_IEEE754(from_base: str, prec: str) -> str:
    '''
    convert dec to bin

    type: u(nsigned), s(igned) or f(raction)
    '''

    from_base = float(from_base)
    prec = int(prec)

    res = ''

    len_e = {
            16: 5,
            32: 8,
            64: 11
        }

    len_m = {
            16: 10,
            32: 23,
            64: 55
        }

    # check if its a special case inf or -inf
    if from_base in ['inf', '-inf']:
            s = '1' if from_base == '-inf' else '0'
            e = '1' * len_e[prec]
            m = '0' * len_m[prec]

            return s + e + m

    str_from_base = str(abs(from_base))
    
    # if number is too small or too big
    if 'e' in str_from_base:
            idx_e = str_from_base.index('e')

            str_exp = str_from_base[idx_e + 1:]
        
            if str_exp[0] == '-':
                if '.' not in str_from_base:
                    str_from_base = format(from_base, f'.{int(str_from_base[idx_e + 2:])}f')
                else:
                    idx_point = str_from_base.index('.')

                    x = len(str_from_base[idx_point + 1:idx_e])
        
                    str_from_base = format(from_base, f'.{int(str_from_base[idx_e + 2:]) + x}f')
            else:
                str_from_base = format(from_base, '.0f')

    int_part, dec_part = str_from_base.split('.')

    # check special cases
    if int(int_part) == 0 and int(dec_part) == 0:
            s = '1' if str(from_base)[0] == '-' else '0'
            e = '0' * len_e[prec]
            m = '0' * len_m[prec]
    else:
            # convert integer part and decimal part to binary
            bin_int_part = bin(int(int_part))[2:]
            
            dec_part_sn = float(dec_part) * pow(10, -len(str(dec_part))) # decimal part in scientific notation from 0001 -> 1e-4
            
            if int(int_part) >= 1:
                bin_dec_part = dec_part_to_bin(dec_part_sn)
            else:
                bin_dec_part = dec_part_to_bin_2(dec_part_sn, prec)
    
            bin_num = bin_int_part + '.' + bin_dec_part
            
            if bin_num[0] == '1':
                idx_dot = bin_num.index('.')

                moves = idx_dot - 1

                bin_num = bin_num.replace('.', '')

                shifted_bin_num = bin_num[0] + '.' +  bin_num[1:]
            else:
                idx_dot = bin_num.index('.')
                idx_one = bin_num.index('1')

                moves = idx_one - idx_dot
            
                shifted_bin_num = bin_num[moves + 1] + '.' +  bin_num[moves + 2:]

                moves = -moves

            bias = {
                16: 5,
                32: 127,
                64: 1023
            }

            # s(ign), e(xponent) and m(antissa)
            s = '1' if from_base < 0 else '0'
        
            e = moves

            e += bias[prec]

    if e <= 0:
                # check denormal number, special case
            if -(len_m[prec] + bias[prec]) <= e - 127 < -bias[prec] - 1:
                    pass
            else:
                    print('ERROR: Maximum normal number representable 2^-126')

                    return False
            
    e = bin(e)[2:]
    
    if len(e) < len_e[prec]:
                bit_to_add = len_e[prec] - len(e)

                e = '0' * bit_to_add + e
    elif len(e) > len_e[prec]:
                print('ERROR: Exponent too large')

                return False
        
    m = shifted_bin_num[2:]
            
            # round mantissa
    if len(m) > len_m[prec]:
                m = m[:len_m[prec] + 1]

                if m[-1] == '0':
                    m = m[:-1]
                else:
                    m = add_one(m[:-1])

    # fill with 0's the mantissa   
    m = m + ('0' * (len_m[prec] - len(m)))
    
    #res = s + '|' + e + '|' + m
    res += s + e + m
    
    return res


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
    except ValueError:
        print("Number not compatible.")
    except PrecisionError:
        print("Precision not supported.")



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
