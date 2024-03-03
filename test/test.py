import time
x = 100
start = time.start()
print(f"{x}roop start")

for i in range(x):
    if i+1 == x:
        end = time.time()
        diff = end - start
        print(f"{x} times roop is finished. time is {diff}")