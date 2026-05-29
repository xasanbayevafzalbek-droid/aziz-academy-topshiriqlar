n = int(input())
c = 0
i = 1
while i <= n:
    if i % 2 == 0:
        c += 1
    i += 1
print(c)