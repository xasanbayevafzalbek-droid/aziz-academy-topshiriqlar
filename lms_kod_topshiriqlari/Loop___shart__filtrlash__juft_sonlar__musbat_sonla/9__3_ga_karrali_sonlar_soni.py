n = int(input())
s = list(map(int, input().split()))
c = sum(1 for x in  s if x % 3 == 0)
print(c)