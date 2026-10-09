'''1. Counting Positive Numbers
Problem: Di gayi numbers ki list numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10] me se sirf positive numbers ko count karein.'''

number = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number = 0

for num in number:
    if(num > 0):
        positive_number += 1
    print("The positive number in given list is :",positive_number)  