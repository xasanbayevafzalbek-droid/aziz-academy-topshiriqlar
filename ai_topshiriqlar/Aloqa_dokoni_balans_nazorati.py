# Aloqa do'koni: balans nazorati
# Kurs: Dasturlash / IT
# Mavzu: Sonlar: int va float — butun va kasr sonlar
# Ball: 100
# Aziz Academy — AI Topshiriq

balans = 100000
e_p = balans
ch = 0
n = int(input())
for _ in range(n):
    amal = input()
    if amal[0] == "+":
        balans += int(amal[1:])
    else:
        balans -= int(amal[1:])
        ch += 1
    if balans < e_p:
        e_p = balans
print(balans)        
print(e_p)
print(ch)