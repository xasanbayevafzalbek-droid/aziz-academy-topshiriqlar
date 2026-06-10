n = int(input())
if n <= 1:
    print(0) 
else:        
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(n // i) 
            break
    else:
        print(1)