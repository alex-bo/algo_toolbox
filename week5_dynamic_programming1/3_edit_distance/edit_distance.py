# Uses python3
from collections import namedtuple
from typing import List, Tuple


Node = namedtuple('Node', ['val', 'parent', 'i', 'j'])


def edit_distance(s: str, t: str) -> int:
    d = [[None for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    for i in range(len(d)):
        for j in range(len(d[i])):
            if i == 0:
                d[i][j] = Node(val=j, parent=d[i][j - 1] if j > 0 else None, i=i, j=j)
            elif j == 0:
                d[i][j] = Node(val=i, parent=d[i - 1][j] if i > 0 else None, i=i, j=j)
            else:
                optimal = min(
                    # up
                    Node(val=d[i - 1][j].val + 1, parent=d[i - 1][j], i=i, j=j),

                    # left
                    Node(val=d[i][j - 1].val + 1, parent=d[i][j - 1], i=i, j=j),

                    # diagonal
                    Node(val=d[i - 1][j - 1].val + (0 if s[i - 1] == t[j - 1] else 1),
                         parent=d[i - 1][j - 1],
                         i=i, j=j),
                    key=lambda n: n.val
                )
                d[i][j] = optimal
    # print_rect(d)
    print_optimal_alignment(s, t, d)
    return d[-1][-1].val


def print_optimal_alignment(s: str, t: str, d: List[List[Node]]):
    print('=' * len(d[0]) * 2)
    stack = []
    backtrack(d[-1][-1], s, t, stack)
    print(' '.join(i for i, _ in stack))
    print(' '.join(i for _, i in stack))


def backtrack(n: Node, s: str, t: str, stack: List[Tuple[str, str]]):
    if not n:
        return
    backtrack(n.parent, s, t, stack)
    if not n.parent:
        return
    if n.i != n.parent.i and n.j != n.parent.j:
        stack.append((s[n.i - 1], t[n.j - 1]))
    elif n.i != n.parent.i:
        stack.append((s[n.i - 1], '-'))
    else:
        # if n.j != n.parent.j:
        stack.append(('-', t[n.j - 1]))


def print_rect(d: List[List[Node]]):
    print('=' * len(d[0]) * 2)
    for i, l in enumerate(d):
        for j in l:
            print(j.val, end=' ')
        print()


def test_one(s: str, t: str, expected: int):
    print(s)
    print(t)
    actual = edit_distance(s, t)
    if actual == expected:
        print('OK')
    else:
        print('WRONG!')
        raise Exception('Expected {}, got {}'.format(expected, actual))


def test():
    test_one('ab', 'ab', 0)
    test_one('short', 'ports', 3)
    test_one('editing', 'distance', 5)


if __name__ == "__main__":
    test()
    print(edit_distance(input(), input()))
