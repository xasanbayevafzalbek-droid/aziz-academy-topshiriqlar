n =int(input())
if n <= 1:
    print("Not Prime")
else:
    i_p = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            i_p = False
            break
    if i_p:
        print("Prime")
    else:    
        print("Not Prime")