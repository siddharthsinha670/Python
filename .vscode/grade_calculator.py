'''grade calculator
A(90- 100)
B(80-89)
c(70-79)
d(60-69)
E(below 60)
'''

score = 90

if( score >=101):
    print("please verify your score")
    exit()
    

if( score <0):
    print("please verify your score")   
    exit() 



if( score >=90 and score <=100):
    print("your grade  is A")

elif( score >= 80 and score <=90):
    print("your grade is B")    

elif( score >= 70 and score <=80):
    print (" your grade is C")

elif(score >=60 and score <=70):
    print("your grade is  D")     

else:
    print("your grade is F ")   

    

     