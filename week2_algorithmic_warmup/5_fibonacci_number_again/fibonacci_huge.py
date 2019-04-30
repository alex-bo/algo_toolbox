# Uses python3
from random import randint


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m


def calc_fib_optimized(num):
    if num == 0:
        return 0
    if num in (1, 2):
        return 1
    n1, n2 = 1, 1
    for _ in range(num - 2):
        n1, n2 = n2, n1 + n2
    return n2


def get_fibonacci_huge_optimized(n, m):
    if n <= 1:
        return n
    period_length = find_period_length(n, m)
    return get_fibonacci_huge_naive(
        n % period_length,
        m
    )


def find_period_length(n: int, m: int) -> int:
    if n <= 1:
        return n
    period_min_length = 3
    period1 = []
    period2 = []
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        p = current % m
        if len(period1) < period_min_length:
            period1.append(p)
        else:
            period2.append(p)
            while len(period1) < len(period2):
                period1.append(period2.pop(0))
            if len(period1) == len(period2):
                if lists_match(period1, period2):
                    return len(period1)
    return n + 1


def lists_match(full: list, part: list):
    if len(full) != len(part):
        raise Exception('Cannot compare lists, length is different!')
    for f, p in zip(full, part):
        if f != p:
            return False
    return True


def test():
    test_period(2015, 3, 8)
    test_period(2015, 2, 3)

    test_one(239, 1000, 161)
    test_one(2816213588, 239, 151)


def test_period(n, m, expected):
    actual = find_period_length(n, m)
    if actual != expected:
        print('WRONG!')
        raise Exception('expected {} got {}'.format(expected, actual))
    else:
        print('OK')


def test_one(a, b, expected):
    actual = get_fibonacci_huge_optimized(a, b)
    if actual != expected:
        print('WRONG!')
        raise Exception('expected {} got {}'.format(expected, actual))
    else:
        print('OK')


def stress_test():
    while True:
        a = randint(10, 10000)
        b = randint(10, 10000)
        print([a, b])
        expected = get_fibonacci_huge_naive(a, b)
        test_one(a, b, expected)


if __name__ == '__main__':
    # test()
    # stress_test()
    nn, mm = map(int, input().split())
    print(get_fibonacci_huge_optimized(nn, mm))
    #
    # for i in (range(121)):
    #     print(get_fibonacci_huge_optimized(i, 10))
