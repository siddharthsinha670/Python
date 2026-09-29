accountBalance = 10000
withdrawalAmount = 5000

if(withdrawalAmount % 100 == 0 and withdrawalAmount <= accountBalance):
    print("You can withdraw your money without any charges")
elif(withdrawalAmount <= 500):
    cash = withdrawalAmount - 10
    print("charges will be appied arount Rs 10.  And Amount in your hand is: Rs",cash)    