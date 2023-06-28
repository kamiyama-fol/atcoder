n=int(input())

if int(n%5) ==int(0):
    print(str(n))
elif int(n%5) <= int(2):
    print(str(n-(n%5)))
elif int(n%5) >= int(3):
    print(str(n+(5-(n%5))))
else:
    print("error")