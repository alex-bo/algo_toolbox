# Uses python3
from random import randint


def gcd_naive(a, b):
    # TODO: finished here
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_optimized(a, b):
    a, b = min(a, b), max(a, b)
    while True:
        a, b = b % a, a
        if a == 0:
            return b


def test():
    test_one(18, 35, 1)
    test_one(28851538, 1183019, 17657)


def test_one(a, b, expected):
    actual = gcd_optimized(a, b)
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
        expected = gcd_naive(a, b)
        test_one(a, b, expected)


def generalizedGCD(num, arr):
    '''
    curr_gcd = 1
    for d in range(2, min(arr)+1):
        print('d={}'.format(d))
        for n in arr[:num]:
            if n % d != 0:
                print('n={} % d={} != 0'.format(n, d))
                break
        else:
            print('max(d={}, curr_gcd={})'.format(d, curr_gcd))
            curr_gcd = max(d, curr_gcd)
    return curr_gcd
    '''
    arr = arr[:num]
    while len(arr) > 1:
        a = arr.pop()
        b = arr.pop()
        arr.append(optimizedGCD(a, b))
    return arr[0]


def optimizedGCD(a, b):
    a, b = min(a, b), max(a, b)
    while True:
        a, b = a % b, a
        if a == 0:
            return b


if __name__ == "__main__":
    print('gcd={}'.format(generalizedGCD(5, [2,4,6,8,10])))
