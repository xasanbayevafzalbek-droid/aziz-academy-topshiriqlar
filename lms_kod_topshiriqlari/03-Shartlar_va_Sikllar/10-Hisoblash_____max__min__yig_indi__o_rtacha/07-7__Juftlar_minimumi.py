n = int(input())
s = [int(x) for x in input().split()]
j_m = None
for i in s:
    if i % 2 == 0:
        if j_m is None or i < j_m:
            j_m = i
if  j_m is None:            
    print("No")
else:
    print(j_m)