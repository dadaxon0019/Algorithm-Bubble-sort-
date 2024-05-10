def buble_sort(arr):    
    for x in range(len(arr) - 1):
        for i in range(len(arr)- 1 - x):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]      
    return arr

res = buble_sort([2,6,0,1,3,4])
print(res)
