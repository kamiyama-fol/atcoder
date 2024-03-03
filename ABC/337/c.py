def gkbv(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key  
n = int(input())
aa = list(map(int,input().split(" ")))
a = {}
line = []
for i in range(n):
    line.append(0)
for i in range(n):
    a[i+1] = aa[i]

line[0] = gkbv(a, -1)

#for i in range(1,n+1):
    


print(line)




