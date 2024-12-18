# This file contains all the printer functions used for displaying messages by
# the main program.

# This function prints information related to decimal-to-IEEE754 converter.
def print_to_IEEE754_information() -> None:
    print()

    print("+------------------------ IEEE754 USAGE -------------------------+")
    print("|                                                                |")
    print("|  Choose one of the following options:                          |")
    print("|                                                                |")
    print("|   - half                             (Half precision: 1-5-10)  |")
    print("|   - single                         (Single precision: 1-8-23)  |")
    print("|   - double                        (Double precision: 1-11-52)  |")
    print("|                                                                |")
    print("|  Note: only the following special values are allowed:          |")
    print("|    '+infinity', '-infinity', '0', 'NaN'                        |")
    print("|                                                                |")
    print("+----------------------------------------------------------------+")


# This function prints information related to IEEE754-to-decimal converter.
def print_from_IEEE754_information() -> None:
    print()

    print("+------------------------ IEEE754 USAGE -------------------------+")
    print("|                                                                |")
    print("|  Half, single and double precision formats are allowed.        |")
    print("|  Remark: in IEEE754 sign is expressed as either 0 or 1.        |")
    print("|  Note: the format chosen will be determined by the exponent's  |")
    print("|        length, make sure to insert 5, 8 or 11 digits.          |")
    print("|                                                                |")
    print("+----------------------------------------------------------------+")


# This function prints information about the project.
def print_information() -> None:
    print()

    print("+------------------------- INFORMATION --------------------------+")
    print("|                                                                |")
    print("|  Authors:                                                      |")
    print("|   Nicolo Alesi                                                 |")
    print("|   Enes Ozdemir                                                 |")
    print("|   Federico Alcantara                                           |")
    print("|   Davide Catucci                                               |")
    print("|                                                                |")
    print("|  License: MIT License                                          |")
    print("|                                                                |")
    print("+----------------------------------------------------------------+")


# This function prints all available modes.
def print_instructions() -> None:
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
    

# This function prints the list of available commands.
def print_header() -> None:
    print()    

    print("+----------------------- NUMBER CONVERTER -----------------------+")
    print("|                                                                |")
    print("|  Use this program to convert numbers.                          |")
    print("|                                                                |")
    print("|  Commands:                                                     |")
    print("|   /convert              - Start the converter                  |")
    print("|   /help                 - Print this message again             |")
    print("|   /information          - Print useful information             |")
    print("|   /exit                 - Close this program                   |")
    print("|                                                                |")
    print("+----------------------------------------------------------------+")
