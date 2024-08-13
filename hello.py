# print("hello World")   
# Input: 
 


arr= [1, 2, 3, 4, 5]
# Output: [3, 2, 1, 5, 4]
k= 3
n = len(arr)
for i in range(0,n,k):
    if i>n-k:
        arr[i:] = reversed(arr[i:])
# print(arr)
    else:
        arr[i:i+k] = reversed(arr[i:i+k])
print(arr)