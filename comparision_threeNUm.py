## Teen numbers input lekar sabse bada number find karo.

firstNum = int(input("Enter the first number :"))
secondNum = int(input("Enter the second number :"))
thirdNum = int(input("Enter the third number :"))

if(firstNum >= secondNum >= thirdNum):
    print("first Number is greater than other number.")
elif(secondNum >= thirdNum >= firstNum):
    print("Second Number is greater than other number.")
elif(thirdNum >= firstNum >= secondNum):
    print("Third number is  greater than other.")
else:
    print("The number is equal to other.")        