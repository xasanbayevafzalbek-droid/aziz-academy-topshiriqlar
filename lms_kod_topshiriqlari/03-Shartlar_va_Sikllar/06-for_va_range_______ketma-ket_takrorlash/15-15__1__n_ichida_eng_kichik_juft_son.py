n = int(input())
e_k_j = None
for i in range(1, n +1):
    if i % 2 == 0:
        e_k_j = i
        break
if e_k_j:        
    print(e_k_j)    
else:
    print("No")
