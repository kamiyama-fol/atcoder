input_line=input()
input_line = input_line.split(" ")
answer=0
for i in range(64):
    #input_line[i]=int(input_line[i])
    answer=answer+int(input_line[i])*2**(i)
print(answer)