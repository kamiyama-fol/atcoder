n, q = map(int, input().split(" "))
t = list(map(int, input().split(" ")))
s = []
for i in range(n):
    s.append(1)



for i in t:
    if s[i-1] == 1:
        s[i-1] = 0
        continue
    elif s[i-1] == 0:
        s[i-1] = 1
        continue

print(s.count(1))
