yashirin_son = 4
urunishlar_soni = 0
while True:
    taxmin = int(input())
    urunishlar_soni += 1
    if taxmin == yashirin_son:
        print(f"Correct in {urunishlar_soni} tries")
        break
