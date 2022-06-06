# q9

# defining function to arrange in ascending order
def asc(string):
    array = string.split()
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print("Enter string (don't forget to leave spaces between the elements to be sorted!)")
a = input("")
print(asc(a))

# tested
