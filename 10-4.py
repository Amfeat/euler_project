from time import time

n = 2000001
start = time()

a = [True] * n
c = int(n ** 0.5) + 1

for i in range(2, c):
    for j in range(i*i, n, i):
        a[j] = False

b = [x for x in range(2, n) if a[x]]

print("Time: ", time() - start)
print(sum(b))

