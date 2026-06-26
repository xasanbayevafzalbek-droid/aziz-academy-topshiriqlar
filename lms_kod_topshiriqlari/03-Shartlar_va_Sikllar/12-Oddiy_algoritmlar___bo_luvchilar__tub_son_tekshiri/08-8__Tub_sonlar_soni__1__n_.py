n = int(input())
count = 0
sieve = [True] * (n + 1) 
for i in range(2, int(n**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, n + 1, i):
            sieve[j] = False
for i in range(2, n + 1):
    if sieve[i]:
        count += 1
print(count)            