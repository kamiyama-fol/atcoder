def same(x):
    for i in range


n = int(input())
d = list(map(int,input().split(" ")))
answer=0
for m in range(n):
    for day in range(d[m]):
        if list(d[m])
            if day+1 == :
                answer +=1
        print(f"{m+1}月{day+1}日")
print(answer)