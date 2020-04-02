def sol(a,sum1):
    curr_sum = a[0]
    start = 0
    for i in range(1,len(a)+1):
        while curr_sum > sum1 and start < i-1:
            curr_sum = curr_sum-a[start]
            start =start + 1
        if curr_sum == sum1:
            print("found at",start,"and",i)
            return 1
        if(i<len(a)):
            curr_sum = curr_sum +a[i]
    print("no subarray")
    return 0

test = int(input())
for i in range(test):
    n, s = map(int, input().split()) 
   
    array = list(map(int,input().split()[:n]))
    print(sol(array,s))

