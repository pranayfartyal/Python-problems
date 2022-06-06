# q1


# function to arrange in ascending order
def asc(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# function to arrange in descending order
def desc(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


# just for convenience, so function doesnt require ""
def none(array):
    return array


# defining function
def arrange(array, action):
    if action == asc:
        return asc(array)
    if action == desc:
        return desc(array)
    if action == none:
        return array


l = []


n = int(input("Enter number of elements : "))


for i in range(0, n):
    x = int(input())

    l.append(x)

a=input("Enter the action you want")
print(arrange(l,a))


# tested
