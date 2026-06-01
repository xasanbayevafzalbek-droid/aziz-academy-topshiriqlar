n = int(input())
s = list(map(int, input().split()))
o = sum(s) / n
k_s_s = sum(1 for x in s if x > o)
print(k_s_s)           