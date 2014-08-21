'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fib(n):
    if n == 1 or n == 2:
        return n
    return fib(n-1) + fib(n-2)

#Find the ending n location
def find_location(max_value):
    loc = 0
    while True: 
        if fib(loc + 1) >= max_value:
            return loc
        else:
            loc += 1

max_location = find_location(4000000)

values = []
for i in range(0,max_location):
    values.append(fib(i+1))

total = 0
for num in values:
    if num % 2 == 0:
        total += num

print(total)