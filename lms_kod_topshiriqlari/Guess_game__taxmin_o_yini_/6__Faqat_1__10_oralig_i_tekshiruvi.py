yashirin_son = 6
urinishlar_soni = 0
while True:
    try:
        taxmin = int(input())
        if taxmin < 1 or taxmin > 10:
            print("Invalid")
            continue
        urinishlar_soni += 1    
        if taxmin == yashirin_son:
            print("Correct")
            break
    except EOFError:
        break