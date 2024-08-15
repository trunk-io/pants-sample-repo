from number_tester.is_prime import is_prime


def try_numbers():
    for i in range(1, 101):
        print(f"{i} is prime: {is_prime.is_prime(i)}")


if __name__ == "__main__":
    print("Hello, World!")
