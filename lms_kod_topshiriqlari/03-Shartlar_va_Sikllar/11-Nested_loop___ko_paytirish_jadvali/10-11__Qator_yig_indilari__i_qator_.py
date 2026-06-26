n, m = map(int, input().split())
u_y = m * (m + 1) // 2
for i in range(1, n + 1):
    q_y = i * u_y
    print(q_y)