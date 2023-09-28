nx = list(int,map(input().split(" ")))
a = list(int, map(input().split(" ")))
scores = sum(a) - a[0] - a[nx[0]-2]
min = nx[1] - scores