# Kalkulyator dasturi
# Kurs: Dasturlash / IT
# Mavzu: 🛠 Mini-loyiha: Kalkulyator — ikki son ustida amallar (CLI)
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
son1, son2, amal = input().split()
son1 = int(son1)
son2 = int(son2)
if amal == '+':
    print(son1 + son2)
elif amal == '-':
    print(son1 - son2)
elif amal == '*':
    print(son1 * son2)
elif amal == '/':    
    print(son1 / son2)