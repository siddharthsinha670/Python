train_type = "Express"
train_coach = "sleeper"
berth_class = "First Ac"
passenger_age = "124"
gender = "male"
distance_km = 24

# input validation
if(distance_km >= 1 and 0 <= int(passenger_age) <= 120):
        print("You are a valid passenger ")
else:
    print("You are a invalid passenger!")        

# Base Fare by Train Type & Class (per km rate):
if(train_type == "Express"):
    if(train_coach == "sleeper"):
        ticket_price = distance_km * 0.64
        print("You have to pay", distance_km)
    elif(train_coach == "3AC"):
        ticket_price = distance_km * 1.40
        print("YOu have to ", ticket_price)
    elif(train_coach == "2AC"):
        ticket_price = distance_km * 2.00
        print("You have  to pay ", ticket_price)   

elif(train_type == "Superfast"):
    if(train_coach == "sleeper"):
        flat_superFast_charges = 45
        ticket_price = distance_km * 0.80 + flat_superFast_charges
        print("You have to pay",ticket_price)
    elif(train_coach == "3AC"):
        flat_superFast_charges = 45
        ticket_price == distance_km *1.70 + flat_superFast_charges
        print("You have to pay",ticket_price) 
    elif(train_coach == "2AC"):
        flat_superFast_charges = 45
        ticket_price == distance_km * 2.40 + flat_superFast_charges
        print("You have to pay",ticket_price)

elif(train_type == "Rajdhani"):
    if(train_coach == "3AC"):
        catering_charges = 300
        ticket_price = distance_km * 2.20 + catering_charges
        print("You have to pay",ticket_price) 

    elif(train_coach == "2AC"):
        catering_charges = 300
        ticket_price =  distance_km * 3.00 + catering_charges
        print("You ticket price will be :", ticket_price)    

# Age & Gender Discounts / Rules:
if(int(passenger_age) <= 5):
    discounted_price = ticket_price * 0
    print("You dont have to pay ticket price.",discounted_price)

elif(int(passenger_age) <= 12):
    discounted_price = ticket_price * (50/100)
    print("You have to pay only 50% of your ticket price",discounted_price)

elif(gender == "male" and int(passenger_age) >= 60):
    discounted_price = ticket_price * (40/100)
    print("You will got a dicount of 40% on your ticket price",discounted_price)

elif(gender == "female" and passenger_age >= 58):
    discounted_price = ticket_price * (50/100)
    print("You will get the discount og 50% on your ticket price", discounted_price)
    
else:
    print("You dont get any discount offer.",ticket_price) 


# taxes and final billing
if(train_coach == "3AC" and  train_coach == "2AC"):
    tax = (5/100)
    final_price = discounted_price + tax
    print("your final price of your ticket is :",final_price)

