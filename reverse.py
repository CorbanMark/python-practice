def reverseString(s):
    reversed = ''
    for char in s:
        reversed = char + reversed
        return reversed
    #For every char fond in s is add to the front of the reversed string