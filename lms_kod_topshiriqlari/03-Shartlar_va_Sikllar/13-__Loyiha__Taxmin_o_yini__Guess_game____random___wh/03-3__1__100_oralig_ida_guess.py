y_s = 42
while True:
    taxmin = int(input())
    if taxmin == y_s:
        print("Correct")
        break 
    elif taxmin < y_s:
        print("Low")
    else:
        print("High")