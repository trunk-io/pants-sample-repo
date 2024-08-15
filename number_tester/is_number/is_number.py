def is_number(input_string):
    if isinstance(input_string, str):
        return input_string.isnumeric()

    if isinstance(input_string, (int, float)):
        return True

    return False
