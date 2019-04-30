# Uses python3
from typing import List
from random import randint


def get_change_naive(coins: List[int], amount: int) -> int:
    cache = dict()
    coins = sorted(coins)[::-1]
    res = find_next(coins, amount, cache)
    return res


def find_next(coins: List[int], amount: int, cache: dict):
    solution = float('inf')
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if amount in cache:
        return cache[amount]
    for c in coins:
        res = find_next(coins, amount - c, cache)
        if -1 < res < solution:
            solution = res + 1
    cache[amount] = -1 if solution == float('inf') else solution
    return cache[amount]


def get_change_dp(coins: List[int], amount: int) -> int:
    min_num_coins = [0 for _ in range(amount + 1)]
    inf = float('inf')
    for m in range(1, len(min_num_coins)):
        min_num_coins[m] = inf
        for c in coins:
            if m >= c:
                num_coins = min_num_coins[m - c] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[amount] if min_num_coins[amount] != inf else -1


def stress_test():
    while True:
        coins = [randint(1, 10) for _ in range(randint(2, 5))]
        amount = randint(20, 100)
        print(coins)
        print(amount)
        test_one(coins, amount, get_change_naive(coins, amount))


def test():
    test_one([1, 2, 5], 11, 3)
    test_one([1, 2, 5], 0, 0)
    test_one([2], 3, -1)
    test_one([3, 4, 5, 6], 3, 1)
    test_one([3, 4, 5, 6], 6, 1)
    test_one([3, 4, 5, 6], 4, 1)
    test_one([3, 4, 5, 6], 20, 4)
    test_one([2, 3, 4, 5, 6], 19, 4)
    test_one([2, 3, 4, 5, 6], 10, 2)
    test_one([2, 3, 4, 5, 6], 100, 17)
    test_one([2, 3, 4, 5, 6], 5969, 995)
    test_one([186, 419, 83, 408], 6249, 20)


def test_one(coins: List[int], amount: int, expected: int):
    actual = get_change_dp(coins, amount)
    if actual != expected:
        print('WRONG!')
        raise Exception('expected {} got {}'.format(expected, actual))
    else:
        print('OK')


def main():
    coins = [int(i) for i in input().split(' ')]
    amount = int(input())
    print(get_change_dp(coins, amount))


if __name__ == '__main__':
    stress_test()
    test()
    # main()
