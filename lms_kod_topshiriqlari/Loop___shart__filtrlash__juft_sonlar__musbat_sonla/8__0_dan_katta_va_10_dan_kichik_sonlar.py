n = int(input())
s = list(map(int, input().split()))
for x in s:
    if 0 < x < 10:
        print(x)