from libraries.exceptions import *
from libraries.unsigned_converters import *
from libraries.signed_converters import *
from libraries.fractional_converters import *
from libraries.message_printers import *
from libraries.IEEE754_utils import get_to_IEEE754_inputs
from libraries.IEEE754_utils import get_from_IEEE754_inputs


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
                result = convert_IEEE754_to_decimal(sign, exp, mant)
            case _:
                print("Mode not valid.")
                return

        if result != None:
            print("Result:", result)

    except ValueError:
        print("Number not compatible.")
    except SignError:
        print("Sign not compatible.")
    except PrecisionError:
        print("Precision not supported.")
    except OverflowError:
        print("Overflow error.")
    except UnderflowError:
        print("Underflow error.")
    except MantissaError:
        print("Mantissa not compatible.")


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
