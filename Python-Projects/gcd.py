'''
    greatest common denominator function
    returns gcd of inputs a and b
'''
def gcd2(a, b):
    x = a
    y = b
    while x != 0:
        if x >= y:
            x = x - y
        elif x < y:
            temp = x
            x = y
            y = temp
    return str(y)

'''
    greatest common denominator function
    that works with any number of inputs
'''
def gcdn(args):
    if (isinstance(args, list)):
        if (len(args) >= 2):
            if (len(args) == 2):
                if (not is_int(args[0]) or not is_int(args[1])):
                    return "All inputs must be integers"
                if (int(args[0].replace(" ", "")) < 0 or int(args[1].replace(" ", "")) < 0):
                    return "All inputs must be positive integers"
                return gcd2(int(args[0]), int(args[1]))
            else:
                if (not is_int(args[0].replace(" ", "")) or not is_int(args[1].replace(" ", ""))):
                    return "All inputs must be integers"
                if (int(args[0].replace(" ", "")) < 0 or int(args[1].replace(" ", "")) < 0):
                    return "All inputs must be positive integers"
                x = int(args[0].replace(" ", ""))
                y = int(args[1].replace(" ", ""))
                i = 1
                while (i < len(args)):
                    x = gcd2(x, y)
                    if (not is_int(args[i].replace(" ", ""))):
                        return "All inputs must be integers"
                    if (int(args[i].replace(" ", "")) < 0):
                        return "All inputs must be positive integers"
                    i = i + 1
                    if (i < len(args)):
                        y = int(args[i].replace(" ", ""))
                return str(x) + "\nrunning time: "
        else:
            return "The input list must be of size greater than 1."
    else:
        return "The input must be a list."

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
