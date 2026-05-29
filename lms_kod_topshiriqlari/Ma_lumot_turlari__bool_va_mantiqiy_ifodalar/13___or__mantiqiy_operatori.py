a_str = input()
b_str = input()

a = a_str.strip().capitalize() == "True"
b = b_str.strip().capitalize() == "False"

print(a and b)