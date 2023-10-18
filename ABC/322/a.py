n = int(input())
s = list(input())
for i in range(n):
    if s[i] == "A" and s[i+1] =="B" and s[i+2] == "C":
        print(i)
        break