n = int(input())
s = [int(x) for x in input().split()]
m = s[0]
m_i = 0
for i in range(n):
    if s[i] > m:
        m = s[i]
        m_i = i
print(m_i)        