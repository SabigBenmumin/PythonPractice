def endcode(s):
    result = ''
    for c in s:
        number = str(ord(c))
        while len(number) < 3:
            number = '0' + number
        result += number
    return result

print(endcode('Cat'))
