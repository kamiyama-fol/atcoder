import math

def culc(val):
    
    for n in range(val):
        for m in range(val):
            if (n**3) + ((m+1)*(m+2)/6) == val:
                return
                break


        
li = []
while True:
    num = int(input())
    if num == 0:
        break
    else:
        li.append(num)
print(li)

for i in li:
    for val in reversed(range(i)):
        culc(val)
    
        
        