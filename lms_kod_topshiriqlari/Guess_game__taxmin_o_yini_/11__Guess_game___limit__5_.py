y_s = 10 
for i in range(5):
    guess = int(input())
    if guess == y_s:
        print("Correct")
        break
    elif guess == y_s:
        print("You win")
        break
else:    
    print("You lost")