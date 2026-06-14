# Kitob do'konidagi kitoblar sonini hisobla
# Kurs: Dasturlash / IT
# Mavzu: input() bilan foydalanuvchidan ma’lumot olish
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
kitoblar = 0
while True:
    try:
        kitob = input()
        if not kitob:
            break
        janr, son = kitob.split()
        kitoblar += int(son)
    except EOFError:
        break
print(kitoblar)