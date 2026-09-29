memberType = "senior".strip()
memberAge = 56
Subscription = 50


if(memberType == "Student"):
    memberAge == "No restriction"
    Discount = 50 - (10/100)
    print("Student will get discount of $10. And finally you have to pay : $",Discount)


elif(memberType == "senior"):
    if(memberAge >= 60):
        Discount = 50 - (15/100)
        print("You will get the discount of 15% . And finally you have to pay : $",Discount)
    else:
        print("you won't get any discount .You have to pay : $",Subscription)    
 

elif(memberType == "Regular"):
    memberAge == "no restriction"
    print("You won't get dicount. You have to pay : $",Subscription)


else:
    print("not a member of gym")
