# This file contains all the exceptions used by the main program.

# This exception is raised whenever the IEEE754 precision chosen is different
# from 'half', 'single' or 'double'. This means also that it is raise when 
# the length of the exponent is different from 5, 8 or 11.
class PrecisionError(Exception):
    ...


# This exception is raised whenever the sign of IEEE754 numbers is different
# than '0' or '1'.
class SignError(Exception):
    ...


# This excpetion is raised whenever a IEEE754 number is too big to be stored.
class OverflowError(Exception):
    ...


# This exception is raised whenever a IEEE754 number is too small to be stored.
class UnderflowError(Exception):
    ...


# This exception is raised whenever the mantissa of a IEEE754 number is longer
# than the maximum length allowed by its precision.
class MantissaError(Exception):
    ...