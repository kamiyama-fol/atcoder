n,k = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
ans = []
for i in a:
    if i%k == 0 :
        ans.append(str(int(i/k)))

print(" ".join(ans))