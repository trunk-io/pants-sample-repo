from number_tester.is_even.is_even import is_even
from number_tester.is_odd.is_odd import is_odd


def is_even_or_odd(input_string):
    if is_even(input_string):
        return "even"
    if is_odd(input_string):
        return "odd"
    return "not a number"
