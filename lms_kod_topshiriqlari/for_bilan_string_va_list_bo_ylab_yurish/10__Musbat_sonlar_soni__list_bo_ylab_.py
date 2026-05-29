n = int(input())
s = list(map(int, input().split()))
m_s_s = 0
for son in s:
    if son > 0:
        m_s_s += 1
print(m_s_s)        