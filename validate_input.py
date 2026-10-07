# validate input
# problem - keep asking the user for input until they enter the a number between 1 to 10


while True:
    number = int(input("Enter the value between 1 and 10 :"))
    if 1 <= number <=10:
        print("Thanks")
        break
    else:
        print("Invalid number , try again")