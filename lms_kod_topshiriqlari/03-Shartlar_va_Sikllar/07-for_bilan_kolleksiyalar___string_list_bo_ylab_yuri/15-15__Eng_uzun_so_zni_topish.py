words = input().split()
e_u = words[0]
for word in words:
    if len(word) > len(e_u):
        e_u = word
print(e_u)