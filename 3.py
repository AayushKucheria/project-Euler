def isPrime(n):
    m = 2
    while m < n:
        if (n % m) == 0:
            return False
        m += 1
    return True


i = 7
largest = 0
number = 600851475143

while number % 2 == 0:
    number /= 2
    print(2)
while number % 3 == 0:
    number /= 3
    print(3)
while number % 5 == 0:
    number /= 5
    print(5)

if (number % 2) != 0:
    while i < number:
        if (number % i) == 0:
            # Checking for prime
            if isPrime(i):
                print(i)

        i += 2
