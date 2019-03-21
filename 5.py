# Q -

# TRY - Multiply all prime nos in list and then check for factor

def getprime(original):
    prime = []
    flag = 0
    for i in original:
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            prime.append(i)
    return prime


print("Enter the higher limit - ")
limit = int(input())
list = [1]
for i in range(2, limit + 1):
    list.append(i)
print("Original List: ", list)
primelist = getprime(list)
print("Prime list: ", primelist)

# primeproduct = 19 * 17 * 13 * 11 * 7 * 5 * 3 * 2
# print("prime product is ", primeproduct)
# print("24 times primeproduct is ", 24 * primeproduct)
# listwithoutprime = [20, 18, 16, 15, 14, 12, 10, 9, 8, 6, 4]
# count = 0
# while count != 11:
#     count = 0
#     for i in listwithoutprime:
#         if primeproduct % i == 0:
#             count += 1
#             print(count)
#         else:
#             break
#     if count != 11:
#         primeproduct += 9699690
#     else:
#         print(primeproduct)
