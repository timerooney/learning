multiples_three = range(0,1000,3)
multiples_five = range(0,1000,5)
multiples_fifteen = range(0,1000,15)

total = 0

for num in multiples_three:
    total += num

for num in multiples_five:
    total += num

for num in multiples_fifteen:
    total -= num

print(total)
