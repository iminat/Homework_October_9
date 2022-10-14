n = input()
def f(n):
    n1 = n+n
    n2 = n+n+n
    return str(int(n)+int(n1)+int(n2))

print(f(f(n)))


