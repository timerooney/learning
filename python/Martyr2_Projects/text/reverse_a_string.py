def reverse_string(string):
    reversed_string = ""
    i = len(string) - 1
    while i >= 0:
        reversed_string += string[i]
        i -= 1
    return reversed_string

string = input("Please enter the string that you would like to be reversed: ")

reversed_string = reverse_string(string)

print(reversed_string)
