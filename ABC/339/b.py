#上 0 右 1 下 2 左 3
#[縦,横,方向]

def tmove():
    if t[2] == 0:
        
        if t[0] == 0:
            t[0] = h-1
        else:
            t[0] -=1
    elif t[2] == 1:
        
        if t[1] == w-1:
            t[1] = 0
        else:
            t[1] += 1
    elif t[2] ==2:
        
        if t[0] == 0:
            t[0] = h-1
        else:
            t[0] += 1
    elif t[2] == 3:
        
        if t[1] ==0:
            t[1] = w-1
        else:
            t[1] -= 1


h,w,n = list(map(int, input().split(" ")))
board = []
for i in range(h):
    board.append([])
    for j in range(w):
        board[i].append(".")
    #[縦,横,方向]
t =[0,0,0]
for i in range(n):
    if board[t[0]][t[1]] ==".":
        board[t[0]][t[1]] = "#"
        if t[2] ==3:
            t[2] =0
        else:
            t[2] +=1
        
        tmove()

    else:
        board[t[0]][t[1]] = "."
        if t[2] ==0:
            t[2] = 3
        else:
            t[2] -=1
        
        tmove()
        
for i in range(h):
    print("".join(board[i]))



