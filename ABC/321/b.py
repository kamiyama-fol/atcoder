nx = list(map(int,input().split(" ")))
a = list(map(int, input().split(" ")))
for i in range(101):
    a.append(i)
    a.sort
    scores = sum(a) - a[0] - a[nx[0]-1]

    if scores == nx[0]:
        print(i)
        break
    if i ==100:
        print(-1)
        break
    scores = 0
print(scores)