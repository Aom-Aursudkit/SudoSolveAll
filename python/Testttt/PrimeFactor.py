import math


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    max_divisor = math.isqrt(num) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False
    return True


def count_prime_divisors(number):
    count = 0

    for i in range(2, number + 1):
        if is_prime(i) and number % i == 0:
            count += 1

    return count


if __name__ == "__main__":
    # Example usage
    print(count_prime_divisors(30))
