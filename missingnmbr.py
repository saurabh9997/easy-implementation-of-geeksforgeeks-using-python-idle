def missing(a):
    a.sort()
    for i in range(len(a)):
        if i not in a:
            return i
    


test = int(input())
for i in range(0,test):
    length = int(input())
    a =[]
    for i in range(0,length):
        b = int(input())
        a.append(b)
    print(missing(a))
