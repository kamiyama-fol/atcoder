n = int(input())
a = list(map(int, input().split(" ")))
log = []




for j in range(n):
    for i in range(n):
        pivot = 0
        if  a[i] < pivot:
            a[i], a[pivot] = a[pivot], a[i]
            log.append(f"{a[pivot]} {a[i]}")
            pivot = i

print(a)
print(len(log))
for i in log:
    print(i)