x = [6, 9, 0, 0, 3, 4]
cnt = 0
for i in range(0, x-1):
    if x[i] != x[i + 1]:
        cnt += 1
        i += 1
    print(i)
