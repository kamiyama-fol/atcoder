s = list(input())
list = {}
for i in s:
    if i not in list:
        list[i] = 1
    else:
        list[i] +=1
print(list)
flag = True
for i in list:
    valc = sum(v == i for v in list.values())
    print(valc)

    if i != 2 or i != 0:
        flag = False
    print(flag)

if flag:
    print("Yes")
else:
    print("No")