n = int(input())
s_s = input().split()
y = 0
c = 0
for s in s_s:
    y += float(s)
    c += 1
o = y / c
print(o)