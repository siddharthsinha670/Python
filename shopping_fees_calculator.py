'''
free for order = 50 or more
for order under 50 charges rs 5
10 for express 

'''

orderPrice = 45
orderType = "express"

if(orderPrice >=50):
    orderType == "stadard or express"
    print("You won't have to pay extra. Your order price is : $",orderPrice)

elif(orderPrice <=50):
    if(orderType == "Standard"):
        totalCharges = orderPrice + 5
        print("you have to extra $5 . And your final price is : $",totalCharges)    
    elif(orderType == "express"):
        totalCharges = orderPrice + 10 
        print("You have to pay extra $10. And your final price is : $", totalCharges)   
