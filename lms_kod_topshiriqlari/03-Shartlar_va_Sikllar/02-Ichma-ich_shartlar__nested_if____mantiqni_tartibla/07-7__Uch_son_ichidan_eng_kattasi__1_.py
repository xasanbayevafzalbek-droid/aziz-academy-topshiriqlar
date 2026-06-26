a, b, c = map(int, input().split())
if a >= c:
    if a >= b:
         print(a)
    else:
         print(b)
else:
    if b >= c:
        print(b)
    else:
        print(c)
