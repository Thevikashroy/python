def rotatedArray(arr,k):
    stack = []
    n = len(arr)
    for i in range(n-k,n):
        stack.append(arr[i])
    for i in range(n-k-1,-1,-1):
        arr[i+k] = arr[i]
    for i in range(k):
        arr[i] = stack.pop()
    return arr
arr=[3,-2,5,4,-3,2,9,8]
k = 3
print(rotatedArray(arr,k))
        