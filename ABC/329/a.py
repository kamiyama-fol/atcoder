n,l = map(int,input().split(" "))
a = map(int, input().split(" "))
count = 0

for i in a:
    if i >= l:
        count +=1
        
print(count)