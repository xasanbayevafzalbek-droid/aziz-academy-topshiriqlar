n = int(input())
s = list(map(int, input().split()))
m_s_s = sum(1 for x in s if x > 0)
print(m_s_s)