'''
Pet Food Recommendation
Problem: Recommend pet food based on animal species and age 
(e.g., Dog: < 2 years - Puppy food, Cat: > 5 years - Senior cat food).

'''
animalName = "Cat"
animalAge = 2


if(animalName == " Dog"):
    if(animalAge >2):
        print("Adult Dog food")
    else:
        print("puppy Food")  

elif(animalName == "Cat"):
    if(animalAge >= 5):
        print("Senior cat Food")
    else:
        print("juniour/Regular food")              


