#値の入力
input_line=input()
input_line2=input()
input_line=input_line.split(" ")
input_line2=input_line2.split(" ")
rinsetu=4
if int(input_line[0]) - int(input_line2[0]) == 0:
    rinsetu=rinsetu-1
if int(input_line[1]) - int(input_line2[1]) ==0:
    rinsetu=rinsetu-1
if int(input_line2[0]) == 1:
    rinsetu=rinsetu-1
if int(input_line2[1]) == 1:
    rinsetu=rinsetu-1
print(str(rinsetu))