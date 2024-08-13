# find duplicate in array
arr = [2,3,1,2,3]
# n = len(arr)
# repeted=[]
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             repeted.append(arr[i])
# print(repeted)


def getElement(arr):
    n = len(arr)
    ans = []
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                ans.append(arr[i])
                return ans


def main():
    n=5
    arr = [2,3,1,2,3]
    ans = getElement(arr)
    print(ans)
main()

    