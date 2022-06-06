# q6

# defining function to determine whether a given number is prime
def prime(a):
    for i in range(1, int(a**0.5)+1):
        if (a % i == 0 and i != a and i != 1) or (a == 1):
            return "false"
    return "true"


# defining the function that prints all numbers in (a1, an) that are prime
def pir(a1, an):
    for i in range(a1, (an+1)):
        if prime(i) == "true":
            print(i)


first_element = int(input("Enter the first number in the range, (this will be included if it is a prime)"))
last_element = int(input("Enter the last number in the range, (this will be included if it is a prime)"))
pir(first_element, last_element)

# tested
