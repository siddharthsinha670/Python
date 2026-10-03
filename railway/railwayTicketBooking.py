# Railway ticket Booking 

# Changeable according to your need
train_type = "Express"
train_coach = "2AC"
passenger_age = 48
gender = "male"
distance_km = 100
tatkal = "yes"

# Passenger Details
print("   ")
print("The details of the passengers are given below :")
print("Train type :", train_type)
print("Train Coach :", train_coach)
print("Passenger age :", passenger_age)
print("Gender :", gender)
print("Distance traveling :", distance_km)
print("Tatkal booking details :", tatkal)
print("--------------------------------------------------")

# 1. Input Validation
age = int(passenger_age)
if distance_km <= 0 or not (1 <= age <= 120):
    print("Invalid passenger or distance input!")   
    exit()

# 2. Base Fare Calculation & Train Specific Surcharges
base_rate = 0.0
train_surcharge = 0.0

if train_type == "Express":
    if train_coach == "sleeper":
        base_rate = 0.60
    elif train_coach == "3AC":
        base_rate = 1.40
    elif train_coach == "2AC":
        base_rate = 2.00
    else:
        print("Invalid coach for Express train.")
        exit()

elif train_type == "Superfast":
    train_surcharge = 45.0  # Flat superfast charge
    if train_coach == "sleeper":
        base_rate = 0.80
    elif train_coach == "3AC":
        base_rate = 1.70
    elif train_coach == "2AC":
        base_rate = 2.40
    else:
        print("Invalid coach for Superfast train.")
        exit()

elif train_type == "Rajdhani":
    train_surcharge = 300.0  # Mandatory catering charge
    if train_coach == "3AC":
        base_rate = 2.20
    elif train_coach == "2AC":
        base_rate = 3.00
    else:
        print("Sleeper coach is not available in Rajdhani train.")
        exit()
else:
    print("Invalid train type.")
    exit()

base_fare = distance_km * base_rate

# 3. Concession / Discount Calculation (Applied on Base Fare only)
discount_pct = 0.0
discount_reason = "No concession"

is_tatkal = str(tatkal).strip().lower() == "yes"

if is_tatkal:
    discount_pct = 0.0
    discount_reason = "Tatkal booking (concessions void)"
else:
    if age < 5:
        discount_pct = 1.0  # 100% discount (Free)
        discount_reason = "Child under 5 (Free - 100% discount)"
    elif 5 <= age <= 12:
        discount_pct = 0.50  # 50% discount
        discount_reason = "Child (5-12 yrs - 50% discount)"
    elif gender.lower() == "female" and age >= 58:
        discount_pct = 0.50  # 50% discount
        discount_reason = "Senior Citizen Female (50% discount)"
    elif gender.lower() == "male" and age >= 60:
        discount_pct = 0.40  # 40% discount
        discount_reason = "Senior Citizen Male (40% discount)"

discount_amount = base_fare * discount_pct
discounted_base_fare = base_fare - discount_amount

# 4. Tatkal Surcharge
tatkal_surcharge = 0.0
if is_tatkal:
    if train_coach == "sleeper":
        tatkal_surcharge = 150.0
    elif train_coach in ["3AC", "2AC"]:
        tatkal_surcharge = 400.0

# 5. Net Fare before Tax
net_fare = discounted_base_fare + train_surcharge + tatkal_surcharge

# 6. GST Calculation (5% on net fare for AC classes, 0% for Sleeper)
if train_coach in ["3AC", "2AC"]:
    gst = net_fare * 0.05
else:
    gst = 0.0

total_payable = net_fare + gst

# 7. Output Detailed Receipt
print("\n================== FARE RECEIPT ==================")
print(f"Base Rate (per km)      : Rs. {base_rate:.2f}")
print(f"Distance Traveled        : {distance_km} km")
print(f"Base Fare               : Rs. {base_fare:.2f}")
print(f"Concession Applied      : {discount_reason}")
print(f"Discount Amount         : -Rs. {discount_amount:.2f}")
print(f"Discounted Base Fare    : Rs. {discounted_base_fare:.2f}")
if train_surcharge > 0:
    print(f"Train Surcharge/Catering: Rs. {train_surcharge:.2f}")
if tatkal_surcharge > 0:
    print(f"Tatkal Surcharge        : Rs. {tatkal_surcharge:.2f}")
print(f"Net Fare (Before Tax)   : Rs. {net_fare:.2f}")
print(f"GST (5% on AC)          : Rs. {gst:.2f}")
print("--------------------------------------------------")
print(f"Total Amount Payable    : Rs. {total_payable:.2f}")
print("==================================================")