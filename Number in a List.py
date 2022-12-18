nums = [8, 2, 3, -1, 7, 7, 3, 2, 4,-9]


def multiply(n):
    total = 1
    for x in n:
        total *= x
    return total


print(multiply(nums))


def add(n):
    total = 0
    for i in n:
        if i > 5:
            total += i
    return total


print(add(nums))


def is_even(q):
    evens = []
    odds = []
    for i in q:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return evens, odds


print(is_even(nums))

