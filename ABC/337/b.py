s = list(input())
Judge = True
for i in range(len(s)-1):
    if s[i] == "B" and s[i+1] =="A":
        Judge = False
    if s[i] == "C" and s[i+1] == "B":
        Judge = False
    if s[i] == "C" and s[i+1] == "A":
        Judge = False
    else:
        continue

if Judge:
    print("Yes")
else:
    print("No")    