s = list(input())
list = {}
for i in s:
    if i not in list:
        list[i] = 1
    else:
        list[i] +=1
flag = True
for i in range(max(list.values())):
    if list.sum(i) != 2 or list.sum(i) != 0:
        flag = False
if flag:
    print("Yes")
else:
    print("No")