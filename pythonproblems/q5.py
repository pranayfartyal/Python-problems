# q5

# defining function to find out duplicate elements
def sfc(array):
    n = len(array)
    for i in range(n):
        for j in range(n):
            if array[i] == array[j] and i != j:
                return array[i]

c=[x for x in range(1,100)]
c.append(5)

print(sfc(c))

# tested
