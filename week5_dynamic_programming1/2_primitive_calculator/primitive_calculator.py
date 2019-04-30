# Uses python3
from typing import List
from time import time
from random import randint


def optimal_sequence_greedy_incorrect(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence_recursive(n) -> List[int]:
    return find_next_sequence(n, {})


def find_next_sequence(n: int, cache: dict) -> List[int]:
    if n == 1:
        return [1]
    if n in cache:
        return cache[n]
    seqs = []
    if n % 3 == 0:
        seqs.append([n // 3] + find_next_sequence(n // 3, cache))
    if n % 2 == 0:
        seqs.append([n // 2] + find_next_sequence(n // 2, cache))
    seqs.append([n - 1] + find_next_sequence(n - 1, cache))
    cache[n] = min(seqs, key=lambda s: len(s))
    return cache[n]


def optimal_sequence_dp(n: int) -> List[int]:
    seqs = [[] for _ in range(n + 1)]
    for n in range(1, len(seqs)):
        local_seqs = []
        if n % 3 == 0:
            local_seqs.append(seqs[n // 3] + [n])
        if n % 2 == 0:
            local_seqs.append(seqs[n // 2] + [n])
        if n > 1:
            local_seqs.append(seqs[n - 1] + [n])
        elif n == 1:
            local_seqs.append([n])
        seqs[n] = min(local_seqs, key=lambda s: len(s))
    return seqs[-1]


def optimal_sequence_dp_memory_optimized(n: int) -> List[int]:
    seqs = [(0, 0) for _ in range(n + 1)]
    for n in range(1, len(seqs)):
        local_seqs = []
        if n % 3 == 0:
            local_seqs.append((n // 3, (seqs[n // 3][1] + 1)))
        if n % 2 == 0:
            local_seqs.append((n // 2, (seqs[n // 2][1] + 1)))
        if n > 1:
            local_seqs.append((n - 1, (seqs[n - 1][1] + 1)))
        elif n == 1:
            local_seqs.append((n - 1, 0))
        seqs[n] = min(local_seqs, key=lambda i: i[1])
    result = [len(seqs) - 1]
    pair = seqs[-1]
    while pair[0] > 0:
        result.insert(0, pair[0])
        pair = seqs[pair[0]]
    return result


def test_one(n: int, expected: List[int]):
    print(n)
    actual = optimal_sequence_dp_memory_optimized(n)
    print(expected)
    print(actual)
    if len(actual) == len(expected):
        print('OK')
    else:
        print('WRONG')
        raise Exception('Expected {}, got {}'.format(expected, actual))


def test():
    test_one(1, [1])
    test_one(5, [1, 2, 4, 5])
    test_one(96234, [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234])


def stress_test():
    while True:
        n = randint(1000000, 1200000)
        start = time()
        expected = optimal_sequence_dp(n)
        print('regular:\t{}s'.format(round(time() - start)))
        start = time()
        actual = optimal_sequence_dp_memory_optimized(n)
        print('optimized:\t{}s'.format(round(time() - start)))
        if len(actual) == len(expected):
            print('OK')
        else:
            print('WRONG')
            raise Exception('Expected {}, got {}'.format(expected, actual))


def main():
    stress_test()
    # n = int(input())
    # sequence = list(optimal_sequence_greedy_incorrect(n))
    # print(len(sequence) - 1)
    # for x in sequence:
    #     print(x, end=' ')


if __name__ == '__main__':
    main()
