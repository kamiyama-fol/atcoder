N = int(input())
S = list(input())
box={}
i = 0
while "A" not in box.values() ==  "B" not in box.values() == "C" not in box.values() == True:
   
   box[i] = S[i]
   i=i+1
print(S)
print(box)
print(len(box))