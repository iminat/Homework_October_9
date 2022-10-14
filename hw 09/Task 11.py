num = int(input)
def counting_single_nums(num):
    x = (list(str(num)))
    cnt = 0
    for i in range(0, len(x)-1):
        if x[i] != x[i + 1]:
            cnt += 1
            i += 1
    print(cnt)

num = int(input())
counting_single_nums(num)
