n = int(input())
s = list(map(int, input().split()))
m_s = s[0]
for son in s:
    if son < m_s:
        m_s = son
print(m_s)