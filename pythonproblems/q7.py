#q7
def freq(element, array):
    c = array.copy()
    for i in array:
        if element != i:
            (c.remove(i))
    return len(c)

def mode(array):
    m = array[0]
    for i in array:
        if freq(i, array)>m:
                m = i
    return m


a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    x = input()
    a.append(x)
print(a)
# input string
