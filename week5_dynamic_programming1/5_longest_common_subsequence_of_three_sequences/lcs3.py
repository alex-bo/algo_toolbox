#Uses python3
from typing import List


def lcs3(a: List[int], b: List[int], c: List[int]) -> int:
    d = []
    for _ in range(len(a) + 1):
        d.append([])
        for _ in range(len(b) + 1):
            d[-1].append([])
            for _ in range(len(c) + 1):
                d[-1][-1].append(0)
    for i in range(len(d)):
        for j in range(len(d[i])):
            for k in range(len(d[i][j])):
                if i == 0 and j == 0:
                    d[i][j][k] = 0
                elif j == 0 and k == 0:
                    d[i][j][k] = 0
                elif i == 0 and k == 0:
                    d[i][j][k] = 0
                else:
                    optimal = max(
                        d[i - 1][j][k],
                        d[i][j - 1][k],
                        d[i][j][k - 1],
                        d[i - 1][j - 1][k],
                        d[i][j - 1][k - 1],
                        d[i - 1][j][k - 1],
                        d[i - 1][j - 1][k - 1] + (0 if (a[i - 1] != b[j - 1] or b[i - 1] != c[k - 1]) else 1)
                    )
                    d[i][j][k] = optimal
    return d[-1][-1][-1]


def test_one(a: List[int], b: List[int], c: List[int], expected: int):
    print(a)
    print(b)
    print(c)
    actual = lcs3(a, b, c)
    if actual == expected:
        print('OK')
    else:
        print('WRONG!')
        raise Exception('Expected {}, got {}'.format(expected, actual))


def test():
    test_one([1, 2, 3], [2, 1, 3], [1, 3, 5], 2)
    test_one([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7], 3)


if __name__ == '__main__':
    # main()
    test()
