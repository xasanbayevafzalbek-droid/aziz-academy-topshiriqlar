n = int(input())
s = [int(x) for x in input().split()]
maksimum = s[0]
minimum = s[0]
for son in s:
    if son > maksimum:
        maksimum = son
    if son < minimum:
        minimum = son
print(maksimum - minimum)        