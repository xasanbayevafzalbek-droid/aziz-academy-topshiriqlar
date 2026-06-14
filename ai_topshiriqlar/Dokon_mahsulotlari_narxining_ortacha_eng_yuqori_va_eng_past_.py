# Do'kon mahsulotlari narxining o'rtacha, eng yuqori va eng past qiymatini hisoblash
# Kurs: Dasturlash / IT
# Mavzu: Loop + hisoblash: maksimum, minimum, yig‘indi, o‘rtacha
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
n = int(input())
prices = list(map(int, input().split()))
o_n = sum(prices) / len(prices)
e_y = max(prices)
e_p = min(prices)
print(f"O'rtacha narx: {o_n}")
print(f"Eng yuqori narx: {e_y}")
print(f"Eng past narx: {e_p}")