from tqdm import tqdm
primeNumbers = []
#600851475144
def findPrime(x):
    B = True
    for i in range(2,int((x**0.5)+1)):
        if x % i == 0:
            B = False
            break
    return B

n = 100000000
i = 2

for i in tqdm (range (1,n)):
    if findPrime:
        primeNumbers.append(i)
    
print(primeNumbers)
print(primeNumbers.pop())


               
