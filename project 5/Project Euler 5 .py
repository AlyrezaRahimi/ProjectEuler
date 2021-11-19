main_number = 1
div = 1
while div < 21:
    if main_number % div == 0:
        div += 1
        continue
    else:
        main_number += 1
        div = 1
print(main_number)
