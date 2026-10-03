firstNum = int(input("Enter the first number :"))
secondNum =int(input("Enter the second number :"))
thirdNum = int(input("Enter the third number :"))

if(firstNum > secondNum):
    print("Second number is greater than first Number :",firstNum)

elif(secondNum > thirdNum):
    print("Third number is greater than second number :", thirdNum)

elif(thirdNum > firstNum):
    print("First number is greater than third number :", firstNum)        

else:
    print("The number is equal")    