


def rotedArray(arr):
    n = len(arr)
    k = 3
    s = arr[n:k-1:-1]
    m = arr[:k]
    return s+m






def main ():
    arr = [3,-2,5,4,-3,2,9,8]
    
    ans = rotedArray(arr)
    print(ans)
main()