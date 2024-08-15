from number_tester.is_number.is_number import is_number
from number_tester.is_even.is_even import is_even

def is_odd(input_string):
    if is_number(input_string):
        return not is_even(input_string)
    return False
