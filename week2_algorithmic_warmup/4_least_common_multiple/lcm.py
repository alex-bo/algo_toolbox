# Uses python3
from random import randint


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b


def lcm_optimized(a, b):
    a, b = min(a, b), max(a, b)
    for l in range(b, a*b + 1, b):
        if l % a == 0:
            return l
    return a*b


def test():
    test_one(6, 8, 24)
    test_one(28851538, 1183019, 1933053046)


def test_one(a, b, expected):
    actual = lcm_optimized(a, b)
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
        expected = lcm_naive(a, b)
        test_one(a, b, expected)


if __name__ == '__main__':
    # test()
    # stress_test()
    aa, bb = map(int, input().split())
    print(lcm_optimized(aa, bb))


