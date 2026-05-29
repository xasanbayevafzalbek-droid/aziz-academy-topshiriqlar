n = int(input())
s = list(map(int, input().split()))
for i in range(n):
    if i > 0 and i % 2 == 0:
        print(i)