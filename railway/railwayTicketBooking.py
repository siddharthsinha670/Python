# Railway ticket Booking 

#changable according to your need
train_type = "Express"
train_coach = "2AC"
passenger_age = "48"
gender = "male"
distance_km = 100
tatkal = "yes"

# passangers Details
print("   ")
print("The details of the passengers are given below :")
print("Train type :",train_type)
print("Train Coach :",train_coach)
print("Passenger age :",passenger_age)
print("Gender :",gender)
print("Distance traveling :",distance_km)
print("tatkal booking details :",tatkal)

# input validation
if(distance_km >= 1 and 0 <= int(passenger_age) <= 120):
        print(" ")
else:
    print("You are a invalid passenger!")   
    exit()     

# Base Fare by Train Type & Class (per km rate):
# Express train
if(train_type == "Express"):
    if(train_coach == "sleeper"):
        ticket_price = distance_km * 0.64
        print("You have to travel :",distance_km)
    elif(train_coach == "3AC"):
        ticket_price = distance_km * 1.40
        print("You have to travel :",distance_km)
    elif(train_coach == "2AC"):
        ticket_price = distance_km * 2.00
        print("You have  to travel :",distance_km)   

# Superfast train
elif(train_type == "Superfast"):
    if(train_coach == "sleeper"):
        flat_superFast_charges = 45
        ticket_price = (distance_km * 0.80) + flat_superFast_charges
        print("Charges of superfast train is added :",flat_superFast_charges)
    elif(train_coach == "3AC"):
        flat_superFast_charges = 45
        ticket_price = (distance_km *1.70) + flat_superFast_charges
        print("Charges of superfast train is added :",flat_superFast_charges) 
    elif(train_coach == "2AC"):
        flat_superFast_charges = 45
        ticket_price = (distance_km * 2.40 )+ flat_superFast_charges
        print("Charges of superfast train is added :",flat_superFast_charges)

# Rajdhani train
elif(train_type == "Rajdhani"):
    if(train_coach == "3AC"):
        catering_charges = 300
        ticket_price = distance_km * 2.20 + catering_charges
        print("Catering charges :",catering_charges) 

    elif(train_coach == "2AC"):
        catering_charges = 300
        ticket_price =  distance_km * 3.00 + catering_charges
        print("Catering charges :",catering_charges) 

    else:
        print("This option is not available in this train.")   
        exit()    

# Age & Gender Discounts / Rules:
if(int(passenger_age) <= 5):
    discounted_price = ticket_price * 0
    print("You dont have to pay ticket price.")
    print("Your have to pay for your ticket is :",discounted_price)

elif(int(passenger_age) <= 12):
    discounted_price = ticket_price * (50/100)
    print("You have to pay only 50% of your ticket price")
    print("You have to pay for your ticket is :",discounted_price)

elif(gender == "male" and int(passenger_age) >= 60):
    discounted_price = ticket_price-(ticket_price * 40/100)
    print("You will got a dicount of 40% on your ticket price.")
    print("You have to pay for your ticket is :",discounted_price)

elif(gender == "female" and int(passenger_age) >= 58):
    discounted_price = ticket_price * (50/100)
    print("You will get the discount of 50% on your ticket price")
    print("You have to pay for your ticket is :",discounted_price)
    
else:
    discounted_price = ticket_price
    print("You dont get any discount offer.")
    print("You have to pay for your ticket is: ",discounted_price) 


# taxes and final billing
if(train_coach == "3AC" or train_coach == "2AC"):
    Gst = discounted_price * 0.05
    final_price = discounted_price + Gst
    print("Gst have been added into your ticket : Rs",Gst)
    print("You have to pay for your ticket after including all taxes :",final_price)

elif(train_coach == "3AC" or train_coach == "2AC"):
    tatkal_cost = 400
    print("The tatkal cost will be added to your ticket price",tatkal_cost)
    final_price = discounted_price + Gst + tatkal_cost
    print("Your final cost will be the affter including the tatkal cost is :", final_price)        

       
else:
    Gst = 0
    final_price = discounted_price
    print("You don't have to pay any tax")
    print("You have to pay for your ticket is :", final_price)

# tatkal ticket 
if(tatkal == "yes"):
    if(train_coach == "sleeper"):
        tatkal_cost = 150
        final_price = discounted_price + Gst + tatkal_cost
        print("Your final cost will be the after adding the tatkal cost is :", final_price)
    elif(train_coach == "3AC" or train_coach == "2AC"):
        tatkal_cost = 400
        print("The tatkal cost will be added to your ticket price", tatkal_cost)
        final_price = discounted_price + Gst + tatkal_cost
        print("Your final cost will be the affter including the tatkal cost is :", final_price)