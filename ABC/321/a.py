n = list(input())

if len(n) == 1:
    answer ="Yes"
else:
    for i in range(int(len(n))-1):
        
        if int(n[i]) > int(n[i+1]):
            answer = "Yes"
        else:
            answer = "No"
            break

print(answer)