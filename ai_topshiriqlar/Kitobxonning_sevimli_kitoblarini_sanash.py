# Kitobxonning sevimli kitoblarini sanash
# Kurs: Dasturlash / IT
# Mavzu: for bilan string va list bo‘ylab yurish
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
kitoblar = [input() for _ in range(n)]
takrorlanish = {}
for kitob in kitoblar:
    if kitob in takrorlanish:
        takrorlanish[kitob] += 1
    else:
        takrorlanish[kitob] = 1
for kitob, soni in takrorlanish.items():
    print(f"{kitob} {soni}")