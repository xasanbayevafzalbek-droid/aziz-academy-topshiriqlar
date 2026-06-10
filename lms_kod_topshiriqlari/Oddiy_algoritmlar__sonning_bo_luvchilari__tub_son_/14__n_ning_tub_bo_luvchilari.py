n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        i_p = all(i % j != 0 for j in range(2, int(i**0.5) + 1))
        if i_p:
            print(i)