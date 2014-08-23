def optimize_change(money_owed):
    change = {2000: 0, 1000: 0, 500: 0, 100: 0, 25: 0, 10: 0, 5: 0, 1: 0}
    #for key in sorted(change, reverse=True):
    remainder = money_owed
    for key in sorted(change,reverse = True):
        denomination_quantity = int(remainder / key)
        change[key] = denomination_quantity

        remainder -= key * denomination_quantity #iterate one more denomination down
        if remainder == 0:
            break #leave the sequence if there is nothing left to be taken care of with lower denominations 
    return change

print(optimize_change(501))

def print_change(change): 
    for key in sorted(change, reverse = True):
        if change[key] > 0:
            denomination_float = key / 100.0
            print("${:.2f}: {}".format(denomination_float, change[key]))

print_change(optimize_change(501))
