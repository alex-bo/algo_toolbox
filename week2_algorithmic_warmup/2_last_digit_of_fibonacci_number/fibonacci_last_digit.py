# Uses python3
from random import randint


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_optimized(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current


if __name__ == '__main__':
    # while True:
    #     num = randint(1, 56)
    #     print(num)
    #     expected = get_fibonacci_last_digit_naive(num)
    #     actual = get_fibonacci_last_digit_optimized(num)
    #     if actual != expected:
    #         print('WRONG!')
    #         break
    #     else:
    #         print('OK')
    num = int(input())
    print(get_fibonacci_last_digit_optimized(num))
