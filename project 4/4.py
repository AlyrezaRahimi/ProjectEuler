final_number = 0
Mo = []
Fi = []

def palindrom():
    for i in str(final_number):
        Mo.append(int(i))
    if Mo[len(Mo) - 1] == Mo[0]:
        if Mo[len(Mo) - 2] == Mo[1]:
            if Mo[len(Mo) - 3] == Mo[2]:
                Fi.append(final_number)
                #print(number_one,number_two," = ",final_number)
            else:
                Mo.clear()
        else:
            Mo.clear()
    else:
        Mo.clear()
    
for number_two in range(100,1000):
    for number_one in range(100,1000):
        final_number = number_one * number_two
        palindrom()
    number_one -= 1  
    number_two -= 1

print(max(Fi))






