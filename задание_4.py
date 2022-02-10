import random

a = []
b = []

for i in range(10):
    a.append(random.randint(0, 30))
    b.append(random.randint(0, 30))

c = []
for i in a:
    if i in c:
        continue
    for j in b:
        if i == j:
            c.append(i)
            break

print(c)