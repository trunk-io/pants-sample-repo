def is_number(input_string):
    if isinstance(input_string, (int, float, str)):
        try:
            float(input_string)
            return True
        except ValueError:
            return False
    return False
