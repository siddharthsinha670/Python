n = int(input("enter the number")) 


for i in range(2, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
