n = int(input())
s_d = sum(i for i in range(1, n) if n % i == 0)
if n > 1 and s_d == n:
    print("Perfect")
else:
    print("Not Perfect")
    