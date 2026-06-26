y_s = 3 
while True:
    taxmin = int(input())
    if taxmin == 0:
        print("Exit")
        break
    elif taxmin == y_s:
        print("Correct")
        break
    elif taxmin > y_s:
        print("High")
    else:
        print("Low")
