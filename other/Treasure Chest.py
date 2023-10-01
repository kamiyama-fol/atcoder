input_line =input()
input_line2 = input()
input_line2 = input_line2.split("|")
input_line2 = list(str(input_line2[1]))

result = "*" in input_line2
if result == True:
    print("in")
elif result == False:
    print("out")
else:
    print("error")