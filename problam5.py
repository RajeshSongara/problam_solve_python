# you are given N stick each of neglibale thichknes and the ith stich has length A[i]
# you have to from rectengle by choosing any four sticks
# find the maximum area of rectangle that is possible


def retengle_area(n_sticks,lengths):
    arr=[]
    for stk in lengths:
        if lengths.count(stk)>=2 and stk not in arr:
            arr.append(stk)
    max_lenght=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j]>max_lenght:
                max_lenght=arr[i]*arr[j] 
    return max_lenght              


print(retengle_area(8,[4,2,3,2,3,4,5,1]))


    