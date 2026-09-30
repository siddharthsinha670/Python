train_type = "Express"
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
if(train_type == "Express" or "Superfast" or "Rajdhani"):
    print(train_type)
    

