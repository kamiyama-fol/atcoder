s = list(input())
list = {}
for i in s:
    if i not in list:
        list[i] = 1
    else:
        list[i] +=1
flag = True
for i in range(max(list.values()) + 1):
    count = sum(v == i for v in list.values())
    print(count)
    if count == 2 or count == 0:
        flag = False
if flag:
    print("Yes")
else:
    print("No")