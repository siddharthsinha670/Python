'''condition 
1) age 18+ ticket price = 12
2) wednesday = extra discount -2
3) CHILD = 8
'''

age  = 19
day = "Monday"
price = 12

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print ("Ticket price for you is $",price)
