y_s = 5
u_s = 0
while True:
    taxmin = int(input())
    u_s += 1
    if taxmin == y_s:
        print(u_s)
        break
