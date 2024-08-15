from number_tester.is_number.is_number import is_number


def is_even(input_string):
    if is_number(input_string):
        return int(input_string) % 2 == 0
    return False
