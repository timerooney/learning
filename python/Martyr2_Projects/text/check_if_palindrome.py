def check_if_palindrome(word):
    is_palindrome = True
    forwards = range(0,len(word) - 1)
    backwards = range(len(word) - 1, 0, -1)
    for i in forwards:
        if word[forwards[i]] != word[backwards[i]]:
            is_palindrome = False
    return is_palindrome

entered_word = input("What word would you liked to be checked? ")
word = entered_word.lower()
if check_if_palindrome(word) == True:
    print("{:s} is a palindrome.".format(entered_word))
else:
    print("{:s} is not a palindrome.".format(entered_word))
