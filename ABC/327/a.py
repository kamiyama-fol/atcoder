n = int(input())
s = list(input())



for i in range(n-1):
    judge1 = s[i] == "a" and s[i+1] == "b"
    judge2 = s[i] =="b" and s[i+1]=="a"
    if (judge1) or (judge2):
        print("Yes")
        break
    elif i == n-2:
        print("No")
        break