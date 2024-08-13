# using kadanes algorithm
# find maximum sum of subArray
def getMaximumSum(arr):
    n = len(arr)
    ans = float('-inf')
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        ans = max(current_sum,ans)
        if current_sum < 0:
            current_sum = 0
    return max(ans,current_sum)



def main():
    arr=[-1,2,3,-8,14,3,-15,6,7,-2,8-13,18]
    ans = getMaximumSum(arr)


    print(ans)
main()


