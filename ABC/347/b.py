import math
s = input()
sample = []
samples = []
c = 0
for i in range(len(s)):
    sample.append("")
for i in range(math.factorial(len(s))):
    sample[i] = s[c]
    if samples.count("".join(sample)) == 0:
        samples.append("".join(sample))
    if i%len(s) == 0:
        c +=1

print(len(samples))
