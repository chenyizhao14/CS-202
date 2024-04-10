# int, int -> string
# Given integer num and base b, converts num to a string representation in base b
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    if num == 0:
        return '0'

    x = num % b
    if x < 10:
        str_x = str(x)
    elif x == 10:
        str_x = 'A'
    elif x == 11:
        str_x = 'B'
    elif x == 12:
        str_x = 'C'
    elif x == 13:
        str_x = 'D'
    elif x == 14:
        str_x = 'E'
    elif x == 15:
        str_x = 'F'

    if x == num:
        return str_x
    else:
        return convert(num // b , b) + str_x




