n = int(input())
s = list(map(int, input().split()))
for son in s:
    if son % 2 == 0:
        print(son)