s = list(map(int, input()))
range = [2, 4, 6, 8, 10, 12 , 14, 16 ]
answer = "Yes"
for i in range:
    if s[i-1] % 2 != 0:
        answer = "No"
print(answer)