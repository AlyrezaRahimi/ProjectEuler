from math import sqrt

for i in range(1,999):
    for j in range(1,999):
        k = sqrt(i ** 2 + j ** 2)
        if i + j + k == 1000 and i **2 + j ** 2 == k ** 2:
            print(i,j,k,"product: ",i*j*k)
            
            
