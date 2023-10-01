import math
input_line=input()
input_line=input_line.split(" ")

major={"A":0,"B":3,"C":4,"D":8,"E":9,"F":14,"G":23}
print(int(abs(major[input_line[1]]-int(major[input_line[0]]))))
