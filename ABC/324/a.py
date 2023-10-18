n=int(input())
a = list(map(int, input().split(" ")))
judge ="Yes"
for i in range(n-1):
    if a[i] != a[i+1]:
        judge = "No"
print(judge)