yashirin_son = 15 
while True:
    taxmin = int(input())
    if taxmin == yashirin_son:
        print("Correct")
        break
    farq = abs(yashirin_son - taxmin)
    if farq < 5:
        print("Close")
    else:
        print("Far")