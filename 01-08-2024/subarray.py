#find maximum sum of subarray 

arr = [2,3,-5,6,7,8]
ans = float("-inf")
n=len(arr)
i = 0
k=3
while i<=(n-k):
    sum=0
    for j in range(i,i+k):
        sum+=arr[j]
    ans = max(ans,sum) 
    i+=1
print(sum)


