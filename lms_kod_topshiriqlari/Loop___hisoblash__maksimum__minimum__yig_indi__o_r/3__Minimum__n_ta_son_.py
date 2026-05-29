n = int(input())
sonlar = list(map(int, input().split()))
minimum = sonlar[0]
for i in sonlar:
    if i < minimum:
        minimum = i       
print(minimum)               