s = list(input())
j = "Yes"
if s[0] != "<" or s[len(s)-1] != ">":
    j = "No"

for i in range(1, len(s)-1):
    if s[i] != "=":
        j = "No"

print(j)