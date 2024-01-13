<<<<<<< HEAD
s = list(str(input()))
answer = []
for i in s:
    answer.append(i)
    answer.append(" ")
    
print("".join(answer))
=======
nx = list(map(int,input().split(" ")))
s=list(map(int,input().split(" ")))
answer = 0
for i in s:
    if nx[1] >=i:
        answer += i
print(answer)
>>>>>>> 3d2a7dd2f2498ebb67c6ede1e61c510ef90a6808
