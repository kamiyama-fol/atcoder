k,g,m = input().split(" ")
answer = 0
waterg = 0
waterm = 0
for i in range(k):
    

    if waterg == g:
        waterg =0
    elif waterm == 0:
        waterm += m
    else:
        waterm 