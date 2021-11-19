pr = []

def find_prime(x):
    T = True
    for y in range(2, int((x**0.5)+1)):
        if x % y == 0:
            T = False
            break
    return T

count = 0
number = 2
 
while count < 10001:
    if find_prime(number):
        pr.append(number)
        count += 1
    number += 1

print(pr.pop())

