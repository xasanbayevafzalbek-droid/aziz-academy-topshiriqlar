y_s = 1
u_s = 0
while True:
    taxmin = int(input())
    u_s += 1
    if taxmin == y_s:
        print("Correct")
        print(u_s)
        break 
    else:
        print("Try again")