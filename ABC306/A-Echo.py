input_line = int(input())
input_line2=list(input())

for i in range(input_line):
    input_line2[i]=input_line2[i]+input_line2[i]
print(''.join(input_line2))