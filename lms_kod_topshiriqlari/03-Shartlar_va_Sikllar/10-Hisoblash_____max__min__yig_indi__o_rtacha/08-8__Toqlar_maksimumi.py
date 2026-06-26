n = int(input())
s = [int(x) for x in input().split()]
t_m = None
for i in s:
    if i % 2 != 0:
        if t_m is None or i > t_m:
            t_m = i
if t_m is None:
    print("No")
else:
    print(t_m)