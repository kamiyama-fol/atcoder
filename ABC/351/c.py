n =int(input())
a = list(map(int, input().split(" ")))

#ball = s**a[i]
for j in range(n):
    for i in range(n-1):
        if i == len(a):
            break
        if sum(a) ==1:
            continue
        elif a[i] != a[i+1]:
            continue
        else:
            a.append(a[i]+a[i+1])
            a[i] = 0
            a[i+1] = 0

for k in range(len(a)):
    if a[i] == 0:
        a.pop(i)

print(len(a))
