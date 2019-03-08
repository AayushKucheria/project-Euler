a = 1
b = 2
c = 3
sum = 2

while c < 4000001:
    c = a + b
    if c % 2 == 0:
        sum += c
    a = b
    b = c

print(sum)
