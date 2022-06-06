def sos(string):
    n = len(string)
    total = 0
    for i in range(n):
        total = total + string[i]
    return total
def ignore(string):
    for i in string:
        if(i.isdigit()==False):
            string.replace('i', '')

def addin(string):
    output = sos(ignore(string))

print(addin("ace456"))
#error