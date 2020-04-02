def most_freq(list):
    if(len(set(list))!=1):
        return -1
    else:
        return max(set(list), key = list.count)
test = int(input())
for i in range(0,test-1):
    lth = int(input())
    list=[]
    for i in range(0,lth):
        b=int(input())
        list.append(b)
    print(most_freq(list))
