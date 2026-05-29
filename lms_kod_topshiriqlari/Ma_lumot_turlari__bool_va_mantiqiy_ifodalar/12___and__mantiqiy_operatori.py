a_str = input()
b_str = input()


a = a_str.strip().capitalize() == "True"
b = b_str.strip().capitalize() == "True"

print(a and b)