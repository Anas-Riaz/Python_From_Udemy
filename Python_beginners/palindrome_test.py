def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


word = input("Enter a single world: ")

if is_palindrome(word):
    print("{} word is palindrome".format(word))
else:
    print("{} word is not a palindrome".format(word))
