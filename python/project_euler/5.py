''' 

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def check():
    for number in range(0,999999999999999,9699690):
        print(number)
        if number % 20 == 0 & number != 0:
            return number

print(check())
