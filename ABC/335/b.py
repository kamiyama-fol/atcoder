n = int(input())
answer = [0,0,0]
i = 2
while True:
    answer[i] += 1
    if answer[0] + answer[1] + answer[2] >= n:
        i = i-1
        answer[i] = 0
        continue
    if answer[0] == n:
        break
    else:
        continue