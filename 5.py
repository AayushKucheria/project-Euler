20, 19, 18, 17, 16, 15, 14, 13, 12, 11,


def check20(n):
    if n % 20 == 0:
        return check19(n)
    return False


def check19(n):
    if n % 19 == 0:
        return check18(n)
    return False


def check18(n):
    if n % 18 == 0:
        return check17(n)
    return False


def check17(n):
    if n % 17 == 0:
        return check16(n)
    return False


def check16(n):
    if n % 16 == 0:
        return check15(n)
    return False


def check15(n):
    if n % 15 == 0:
        return check14(n)
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


lim1 = i = 1860480
lim2 = 360360
product = lim1 * lim2
flag = 0
while flag != 1 and i < product:
    if check20(i):
        print(i)
        flag = 1
    print(i)
    i += 1
