n  = int(input())
x = 0
y  = 0
for i in range(n):
    xx, yy =  map(int,input().split(" "))

    x += xx
    y += yy

if x>y:
    print("Takahashi")
elif x ==y:
    print("Draw")
else:
    print("Aoki")