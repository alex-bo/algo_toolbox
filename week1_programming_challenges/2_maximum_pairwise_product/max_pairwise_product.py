# python3
import random


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    i1, n1 = -1, -1
    n2 = -1
    for i, n in enumerate(numbers):
        if n > n1:
            i1 = i
            n1 = n
    for i, n in enumerate(numbers):
        if i != i1 and n > n2:
            n2 = n
    return n1 * n2


if __name__ == '__main__':
    # while True:
    #     n = random.randint(2, 10)
    #     lst = [random.randint(1, 1000000) for _ in range(n)]
    #     print(n)
    #     print(lst)
    #     expected = max_pairwise_product(lst)
    #     actual = max_pairwise_product_fast(lst)
    #     if actual != expected:
    #         print('WRONG!')
    #         break
    #     else:
    #         print('OK')
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
