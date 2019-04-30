# Uses python3
from collections import namedtuple
from typing import List, Tuple

Node = namedtuple('Node', ['val', 'parent', 'i', 'j', 'matches'])


def lcs2(a: List[int], b: List[int]) -> int:
    d = [[None for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(len(d)):
        for j in range(len(d[i])):
            if i == 0:
                d[i][j] = Node(val=j, parent=d[i][j - 1] if j > 0 else None, i=i, j=j, matches=0)
            elif j == 0:
                d[i][j] = Node(val=i, parent=d[i - 1][j] if i > 0 else None, i=i, j=j, matches=0)
            else:
                optimal = min(
                    # up
                    Node(val=d[i - 1][j].val + 1, parent=d[i - 1][j], i=i, j=j, matches=d[i - 1][j].matches),

                    # left
                    Node(val=d[i][j - 1].val + 1, parent=d[i][j - 1], i=i, j=j, matches=d[i][j - 1].matches),

                    # diagonal
                    Node(val=d[i - 1][j - 1].val + (0 if a[i - 1] == b[j - 1] else 1),
                         parent=d[i - 1][j - 1],
                         i=i, j=j, matches=d[i - 1][j - 1].matches + (0 if a[i - 1] != b[j - 1] else 1)),
                    key=lambda n: n.val
                )
                d[i][j] = optimal
    print_rect(d)
    print_optimal_alignment(a, b, d)
    return d[-1][-1].matches


def print_optimal_alignment(a: List[int], b: List[int], d: List[List[Node]]):
    print('=' * len(d[0]) * 2)
    stack = []
    backtrack(d[-1][-1], a, b, stack)
    print(' '.join(i for i, _ in stack))
    print(' '.join(i for _, i in stack))


def backtrack(n: Node, a: List[int], b: List[int], stack: List[Tuple[str, str]]):
    if not n:
        return 0
    backtrack(n.parent, a, b, stack)
    if not n.parent:
        return 0
    if n.i != n.parent.i and n.j != n.parent.j:
        stack.append((str(a[n.i - 1]), str(b[n.j - 1])))
    elif n.i != n.parent.i:
        stack.append((str(a[n.i - 1]), '-'))
    else:
        # if n.j != n.parent.j:
        stack.append(('-', str(b[n.j - 1])))


def print_rect(d: List[List[Node]]):
    print('=' * len(d[0]) * 2)
    for i, l in enumerate(d):
        for j in l:
            print('{}({})'.format(j.val, j.matches), end=' ')
        print()


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(lcs2(a, b))


def test():
    test_one([2, 7, 5], [2, 5], 2)
    test_one([7], [1, 2, 4], 0)
    test_one([2, 7, 8, 3], [5, 2, 8, 7], 2)
    test_one([1, 2, 3, 4, 5, 4, 5, 4, 5, 4], [1, 2, 3, 5, 6, 5, 6, 5, 6], 6)


def test_one(a: List[int], b: List[int], expected: int):
    print(a)
    print(b)
    actual = lcs2(a, b)
    if actual == expected:
        print('OK')
    else:
        print('WRONG!')
        raise Exception('Expected {}, got {}'.format(expected, actual))


if __name__ == '__main__':
    # main()
    test()
