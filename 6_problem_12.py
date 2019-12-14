s = input("Please enter the string: ")


def is_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
        
    return True


if is_palindrome(s):
    print("Palindrome")
else:
    print("Not palindrome")

