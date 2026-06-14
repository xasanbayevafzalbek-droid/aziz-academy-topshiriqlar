# Do'kondagi mahsulotlarni hisoblash
# Kurs: Dasturlash / IT
# Mavzu: while sikli: asoslar
# Ball: 100
# Aziz Academy — AI Topshiriq

while True:
    try:
        n = int(input())
        if n == 0:
            break
        print(f"Mahsulotlar soni: {n}")    
    except EOFError:    
        break