# Q - What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Concept Used - Multiply prime numbers and keep adding base value until all non-prime numbers are factors
# Concept Not Used - Tried finding generalized patters in prime+non-prime numbers. Failed.

def getprime(original):
    prime = []
    for i in original:
        flag = 0
        j = 2
        while j < i and flag == 0:
            if i % j == 0:
                flag = 1
            j += 1
        if flag == 0:
            original.remove(i)
            prime.append(i)
    return original, prime


# Can be changed as per use
high = 20

originallist = []
for i in range(2, high + 1):
    originallist.append(i)

notprimelist, primelist = getprime(originallist)

primebaseproduct = 1
for i in primelist:
    primebaseproduct *= i
primeproduct = primebaseproduct

count = 0
while count != len(notprimelist):
    count = 0
    for i in notprimelist:
        if primeproduct % i == 0:
            count += 1
            print(count)
        else:
            break
    if count != len(notprimelist):
        primeproduct += primebaseproduct
    else:
        print(primeproduct)
