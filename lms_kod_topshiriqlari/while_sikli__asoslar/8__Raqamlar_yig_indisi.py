n = int(input())
yigindi = 0
while n > 0:
    oxirgi_raqam = n % 10
    yigindi += oxirgi_raqam
    n = n // 10 
print(yigindi)


