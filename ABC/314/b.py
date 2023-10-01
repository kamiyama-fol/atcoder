n=int(input())
c=[]
a=[]
for i in range(1, n+1):
    c.insert(i,int(input()))
    a.insert(i,input().split(" "))
x=str(input())

k=int(0)
for i in a:
    if x in i == True:
        k = k+1
print(k)
