n = int(input())
s = list(map(int, input().split()))
t_s = sum(x for x in s if x % 2 != 0)
print(t_s)
