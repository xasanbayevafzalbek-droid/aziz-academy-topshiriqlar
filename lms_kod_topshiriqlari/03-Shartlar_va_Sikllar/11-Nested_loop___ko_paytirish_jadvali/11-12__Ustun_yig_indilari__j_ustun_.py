n, m = map(int, input().split())
q_y = n * (n +1) // 2 
for j in range(1, m + 1):
    u_y = j * q_y
    print(u_y)