<<<<<<< HEAD
s = str(input())

for i in range(len(s)):
    flag = False
    if s[i] == "|" and not flag:
        flag == True
    
=======
s = list(input())
start = s.index("|")
s.pop(start)
end = s.index("|")
s.pop(end)
del s[start:end]
print("".join(s))
>>>>>>> 3874c970735e5f8e3aec89414544eab9a81ae366
