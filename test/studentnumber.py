import random


while True:
    number = []

    number.append(random.randint(2,3))

    for i in range(1,6):
        number.append(random.randint(0,9))



    if sum(number) % 10 == 0:
        number = "".join(str(number))
        print(number)
        break
    else:
        continue

quit()

