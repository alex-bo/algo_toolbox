# Uses python3
from random import randint


period = (0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1,
          6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0)


def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    s = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        s += current
    return s % 10


def fibonacci_sum_optimized(n):
    return period[n % len(period)]


def test():
    test_one(3, 4)
    test_one(121, 1)


def test_one(a, expected):
    actual = fibonacci_sum_optimized(a)
    if actual != expected:
        print('WRONG!')
        raise Exception('expected {} got {}'.format(expected, actual))
    else:
        print('OK')


def stress_test():
    while True:
        a = randint(2, 10000)
        print(a)
        expected = fibonacci_sum_naive(a)
        test_one(a, expected)


if __name__ == '__main__':
    # test()
    # stress_test()
    aa = int(input())
    print(fibonacci_sum_optimized(aa))
    # s = ''
    # for n in range(1000):
    #     s += ' {}'.format(fibonacci_sum_naive(n))
    # print(s)
