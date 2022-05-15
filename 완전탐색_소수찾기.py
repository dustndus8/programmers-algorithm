from itertools import permutations


def solution(numbers):
    answer = 0
    number_list = list(numbers)
    permL = []

    for i in range(1, len(numbers) + 1):
        permL += list(permutations(number_list, i))
    arr = [int(("").join(p)) for p in permL]
    arr = list(set(arr))

    for i in arr:
        if isPrime(i):
            answer += 1
    return answer


def isPrime(a):
    if a <= 1:
        return False
    i = 2
    while i <= a // 2:
        if a % i == 0:
            return False
        i += 1
    return True