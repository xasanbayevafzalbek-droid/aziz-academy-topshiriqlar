n = int(input())
s = list(map(int, input().split()))
a, b = map(int, input().split())
sanoq = 0
for x in s:
    if a <= x <= b:
        sanoq = sanoq + 1
print(sanoq)        