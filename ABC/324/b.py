def prime_factorize(m):
    a = []
    while m % 2 == 0:
        a.append(2)
        m //= 2
    f = 3
    while f * f <= m:
        if m % f == 0:
            a.append(f)
            m //= f
        else:
            f += 2
    if m != 1:
        a.append(m)
    return a

n = int(input())
if max(prime_factorize(n)) == 3 or max(prime_factorize(n)) ==2:
    print("Yes")
else:
    print("No")