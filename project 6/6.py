sum_one = 0
sum_two = 0
one = 1

while one < 101:
    sum_one = sum_one + (one ** 2)
    one += 1

for i in range(1,101):
    sum_two = sum_two + i

sum_two = sum_two ** 2

print("Ekhtelaf is: ",(sum_two - sum_one))