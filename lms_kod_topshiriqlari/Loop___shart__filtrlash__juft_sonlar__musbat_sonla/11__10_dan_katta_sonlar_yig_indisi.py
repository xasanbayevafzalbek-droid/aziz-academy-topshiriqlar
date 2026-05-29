n = int(input())
s = list(map(int, input().split()))
yigindi = 0
for x in s:
    if x > 10:
        yigindi = yigindi + x
print(yigindi)