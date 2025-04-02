def is_palindrome(s):
    if list(s) == list(reversed(s)):
        return True
    return False

s = input()
print(is_palindrome(s))