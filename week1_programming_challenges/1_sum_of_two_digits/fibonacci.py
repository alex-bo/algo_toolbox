# Uses python3
from random import randint


def calc_fib(num):
    if num <= 1:
        return num
    return calc_fib(num - 1) + calc_fib(num - 2)


def calc_fib_optimized(num):
    if num == 0:
        return 0
    if num in (1, 2):
        return 1
    n1, n2 = 1, 1
    for _ in range(num - 2):
        n1, n2 = n2, n1 + n2
    return n2


if __name__ == '__main__':
    # while True:
    #     n = randint(1, 30)
    #     print(n)
    #     expected = calc_fib(n)
    #     actual = calc_fib_optimized(n)
    #     if actual != expected:
    #         print('WRONG!')
    #         break
    #     else:
    #         print('OK')
    n = int(input())
    print(calc_fib_optimized(n))
