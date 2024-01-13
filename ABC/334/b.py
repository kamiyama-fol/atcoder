a, m, l ,r = map(int,input().split(" "))

r_to_a = abs((r - a) // m)

l_to_a = abs((a - l) // m)

print(r_to_a + l_to_a)