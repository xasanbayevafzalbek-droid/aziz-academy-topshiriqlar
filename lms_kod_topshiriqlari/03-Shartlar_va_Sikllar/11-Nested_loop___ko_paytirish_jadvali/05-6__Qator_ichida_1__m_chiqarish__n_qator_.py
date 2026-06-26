n = input().split()
if len(n) == 1:
    print(0)
else:
    a,b = map(int, n)
    if a == b:
        print(1)
    else:
        print(0)