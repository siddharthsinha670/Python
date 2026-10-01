train_type = "Express"
train_coach = "sleeper"
berth_class = "First Ac"
passenger_age = "24"
gender = "male"
distance_km = 24

# input validation
if(distance_km > 0 and passenger_age <= 120):
    print("They are valid passsenger")
else:
    print("please input the valid detiails !")

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
        catering_charges == 300
        ticket_price == distance_km * 3.00 + catering_charges
        print("You ticket price will be :", ticket_price)    


