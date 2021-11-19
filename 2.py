n = 600851475143
i = 2
while i + 1 < n:
    while n % i == 0:
        n = n / i
        print("i is: ",i)
        print("n is: ",n)
    i = i + 1
    #print("i is: ",i)
#print(n)