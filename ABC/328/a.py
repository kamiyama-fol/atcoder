nx = list(map(int,input().split(" ")))
s=list(map(int,input().split(" ")))
answer = 0
for i in s:
    if nx[1] >=i:
        answer += i
print(answer)