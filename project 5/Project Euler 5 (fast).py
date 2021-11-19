i = 1
for k in (range(1, 21)):
    if i % k > 0:
        print("i/k = " ,i/k)
        for j in range(1, 21):
            if (i*j) % k == 0:
                print("(i*j) % k = " ,(i*j) / k)
                i *= j
                print(i)
                break

