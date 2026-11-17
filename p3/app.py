import time
print("starting cpu intensive task....",flush=True)
start = time.time()
x=0
while time.time() - start < 10:
    for i in range(10000):
        x+=i*i

print("task completed")