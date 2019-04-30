# Uses python3
from random import randint

period = (0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7,
          5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1)


def fibonacci_partial_sum_naive(from_, to):
    sum_ = 0

    current = 0
    next_ = 1

    for i in range(to + 1):
        if i >= from_:
            sum_ += current

        current, next_ = next_, current + next_

    return sum_ % 10


def fibonacci_partial_sum_optimized(from_, to):
    return sum(period[i % len(period)] for i in range(from_, to + 1)) % 10


def test_one(a, b, expected):
    actual = fibonacci_partial_sum_optimized(a, b)
    if actual != expected:
        print('WRONG!')
        raise Exception('expected {} got {}'.format(expected, actual))
    else:
        print('OK')


def stress_test():
    while True:
        a = randint(2, 10)
        b = randint(11, 20)
        print(a, b)
        expected = fibonacci_partial_sum_naive(a, b)
        test_one(a, b, expected)


if __name__ == '__main__':
    # stress_test()
    from__, to__ = map(int, input().split())
    print(fibonacci_partial_sum_optimized(from__, to__))
