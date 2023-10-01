s = list(input())
for i in s:
   if i == "a" or i == "i" or i =="u" or i == "e" or i == "o":
        s.remove(i)
        print("".join(s))
print("".join(s))