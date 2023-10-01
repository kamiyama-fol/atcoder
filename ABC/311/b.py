input_line=input()
input_line=input_line.split(" ")
S={}
for i in range(int(input_line[0])):
    S[i] = list(input())
print(S)
count=0
for i in range(int(input_line[1])):
    for c in range(input_line[0]):
        if S[i][c] == "o":
            count=count+1