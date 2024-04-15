s = list(input())
start = s.index("|")
s.pop(start)
end = s.index("|")
s.pop(end)
del s[start:end]
print("".join(s))