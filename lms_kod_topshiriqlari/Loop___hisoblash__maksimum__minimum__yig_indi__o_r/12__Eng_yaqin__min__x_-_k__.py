n = int(input())
a = list(map(int, input().split()))
k = int(input())
b = a[0]
for x in a:
    if abs(x - k) < abs(b - k):
        b = x
    elif abs(x - k) == abs(b - k) and x < b:
        b = x
print(b)        