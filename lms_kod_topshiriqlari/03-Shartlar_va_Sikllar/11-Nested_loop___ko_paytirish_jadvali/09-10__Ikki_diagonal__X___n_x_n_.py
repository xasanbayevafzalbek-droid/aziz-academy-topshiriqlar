n = int(input())
for i in range(n):
    qator = ""
    for j in range(n):
        if i == j or i + j == n - 1:
            qator += "*"
        else:
            qator += "."
    print(qator)
