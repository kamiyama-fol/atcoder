input_line = list(map(int, input().split(" ")))
m = input_line[0]
n = input_line[1]
p = input_line[2]

for i in range(1, n+1):
    if m + i*p <= n:
        print(i)
    if i ==n:
        print(0)