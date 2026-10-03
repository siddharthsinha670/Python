
▼ 23. Railway Ticket Booking & Fare Billing Engine
Problem: Calculate final train fare based on travel class, train category, age/gender concessions, booking quota, and taxes.

Input Constraints:
- Distance: distance_km > 0
- Age: 1 <= passenger_age <= 120
- Terminate with an error message if invalid.

Rate Rules (per km):
- Express: Sleeper - ₹0.60, 3AC - ₹1.40, 2AC - ₹2.00
- Superfast: Sleeper - ₹0.80, 3AC - ₹1.70, 2AC - ₹2.40 (Additional flat surcharge: ₹45)
- Rajdhani: 3AC - ₹2.20, 2AC - ₹3.00 (Mandatory catering: ₹300, Sleeper not available / error)

Concession Rules (Applied on Base Fare only):
- Child (< 5 yrs): Free (100% discount)
- Child (5-12 yrs): 50% discount
- Senior Citizen Female (>= 58 yrs): 50% discount
- Senior Citizen Male (>= 60 yrs): 40% discount
- Only one maximum concession applies per passenger.

Tatkal Booking Rules:
- If Tatkal is 'Yes': All age/gender concessions are void (0% discount).
- Extra surcharge: ₹150 for Sleeper, ₹400 for AC classes (3AC, 2AC).

Taxation:
- Add 5% GST on the total net fare for AC classes (3AC, 2AC). No GST on Sleeper.
- Output a detailed receipt showing Base Fare, Discount, Surcharges, GST, and Total Payable.


### Key Concepts Covered
* **Input Validation & Guard Clauses:** `if distance_km <= 0 or not (1 <= passenger_age <= 120): exit()` ka use karke invalid data ko shuru me hi reject karna.
* **Nested Conditionals:** Train type ke andar specific coach classes ko safely evaluate karna.
* **Multiple Condition Handling (`and`, `or`, `in`):** Complex criteria (jaise gender + age combination, AC classes check karna) ko effectively handle karna.
* **State & Flag Based Overrides:** Tatkal flag (`Yes`/`No`) ke basis par general discount rules ko bypass karna aur extra surcharges add karna.
* **Mathematical Precedence & Business Logic:** Base rate calculation, discount deduction, flat surcharge addition, aur aakhir me conditional tax (GST) calculate karne ka sequential order follow karna.