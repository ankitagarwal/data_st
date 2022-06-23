doors = [False] * 100

for i in range(100):
    print ("{} th pass".format(i+1))
    for j in range(100):
        if (j+1) % (i+1) == 0:
            doors[j] = not doors[j]

print(doors)
print(sum(doors))
for i in range(100):
    if doors[i]:
        print(i+1)


