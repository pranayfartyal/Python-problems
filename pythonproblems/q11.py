def reverse(string):
    n = len(string)
    for i in range(n):
        string[i] = string[n-i-1]
    return string
def palindrome(string):
    if (reverse(string) == string):
        return "True"
    else:
        return "False"

print(palindrome(["1234321"]))
