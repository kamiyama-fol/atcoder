n,s,k = map(int,input().split(" "))
answer=0
for i in range(n):
    p,q = map(int,input().split(" "))
    answer += p*q

if answer < s:
    answer += k
print(answer)

