import math

9, 9, 7, 6, 5, 4, 14, 13, 12, 11,


def check9(n):
    if n % 9 == 0:
        return check8(n)
    return False


def check8(n):
    if n % 8 == 0:
        return check7(n)
    return False


def check7(n):
    if n % 7 == 0:
        return check6(n)
    return False


def check6(n):
    if n % 6 == 0:
        return check5(n)
    return False


def check5(n):
    if n % 5 == 0:
        return check4(n)
    return False


def check4(n):
    if n % 4 == 0:
        return True
    return False


def check14(n):
    if n % 14 == 0:
        return check13(n)
    return False


def check13(n):
    if n % 13 == 0:
        return check12(n)
    return False


def check12(n):
    if n % 12 == 0:
        return check11(n)
    return False


def check11(n):
    if n % 11 == 0:
        return True
    return False


# Factors - 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
# Unique Factors - 5, 7, 9, 11, 13, 16, 17, 19
# Lowest Multiple - 232792560

# Not optimal.
# factors = [19, 17, 16, 13, 11, 9, 7, 5]
# lim1 = i = math.factorial(20)
# i = 323323
# flag = 0
# while flag != 8:
#     for j in factors:
#         if i % j:
#
#             flag += 1
#     i += 323323
# print(i)

# TODO: I need to find Unique factors for myself and multiply them to get the lowest multiple

# Finding unique factors of 10 - 9, 8, 7, 5
factorial10 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in factorial10:
    j = 2
    count = 0
    limit = i / 2
    temp = 0
    factor = []
    while j <= limit:
        if i % j == 0:
            count += 1
            factor.append(j)
        j += 1
    if count > 1 and:
        factorial10.remove(i)
    if count == 1:
        factorial10.remove(temp)

print(factorial10)
