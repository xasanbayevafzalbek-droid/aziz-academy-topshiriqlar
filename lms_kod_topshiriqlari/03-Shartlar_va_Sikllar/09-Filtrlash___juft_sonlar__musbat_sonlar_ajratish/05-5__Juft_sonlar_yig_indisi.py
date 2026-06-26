n = int(input())
s = list(map(int, input().split()))
j_y = sum(x for x in s if x % 2 == 0)
print(j_y)