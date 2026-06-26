s_num = 7
while True:
    n = int(input())
    if n < s_num:
        print("Low")
    elif n > s_num:
        print("High")
    else:
        print("Correct")
        break