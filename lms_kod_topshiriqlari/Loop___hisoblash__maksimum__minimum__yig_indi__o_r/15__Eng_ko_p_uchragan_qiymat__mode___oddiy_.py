n = int(input())
num = list(map(int, input().split()))
ans = num[0]
for x in num:         
    if num.count(x) > num.count(ans):
        ans = x
    elif num.count(x) == num.count(ans) and x <ans:
        ans = x
print(ans)        