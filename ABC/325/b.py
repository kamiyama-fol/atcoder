n = int(input())
wx = []
for i in range(n):
    wx.append(list(map(int, input().split(" "))))

w = []
x = []
for i in range(n):
    w.append(int(wx[i][0]))
    x.append(int(wx[i][1]))
groups = []