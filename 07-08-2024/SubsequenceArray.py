def Subsequence(arr,index,ans):
    if index == len(arr):
        print(ans)
        return

    Subsequence(arr,index+1,ans+[arr[index]])
    Subsequence(arr,index+1,ans)


def main():
    arr = [1, 2, 3]
    index = 0
    ans =[]
    Subsequence(arr,index,ans)
main()