n = int(input())
s = list(map(int, input().split()))
max_val = s[0]
min_val = s[0]
for i in s:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i
print(max_val, min_val)        