# q10

# swapping variables using xor
x = int(input("enter first number"))
y = int(input("enter second number"))
x = (x ^ y)
y = (x ^ y)
x = (x ^ y)

print(x)
print(y)

