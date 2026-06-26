n = int(input())
s = [int(x) for x in input().split()]
m_y = 0
for i in s:
    if i > 0:
        m_y += i
print(m_y)