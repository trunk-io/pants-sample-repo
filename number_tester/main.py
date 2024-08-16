from number_tester.is_even_or_odd.is_even_or_odd import is_even_or_odd


def try_numbers():
    for i in range(1, 101):
        print(f"{i} is even or odd: {is_even_or_odd(i)}")


if __name__ == "__main__":
    print("Hello, World!")
