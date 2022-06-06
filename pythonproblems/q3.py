# q3


# defining calculator function,
def calc(a, o, b):
    if o == "+":
        return a + b
    if o == "-":
        return a - b
    if o == "*":
        return a * b
    if o == "/" and b == 0:  # since division by 0 is not defined
        return "not defined"
    else:
        return a / b


# tested
