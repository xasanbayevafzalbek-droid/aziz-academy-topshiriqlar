n = int(input())
s = list(map(int, input().split()))
for x in s:
    if x % 2 == 0 or x < 0:
        print(x)