def palindrome(n):
    opp = 0
    original = n
    while n > 0:
        temp = n % 10
        n /= 10
        n = int(n)
        opp = (opp * 10) + temp
    if opp == original:
        return True
    else:
        return False


i = 999
j = 999
flag = 0
while (i > 99) and (flag == 0):
    while (j > 99) and (flag == 0):
        product = i * j
        if palindrome(product):
            print(i, " and ", j)
            print(product)
            flag = 1
            break
        j -= 1
    i -= 1
