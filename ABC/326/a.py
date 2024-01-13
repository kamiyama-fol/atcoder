x,y = map(int, input().split(" "))

up = x > y and x - y <= 3
down = x < y and y-x <= 2


if up or down:
    print("Yes")
else:
    print("No")