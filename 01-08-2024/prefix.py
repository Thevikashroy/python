def getOptimizedQueriesResult(arr,queries):
    ps = [0 for i in range(len(arr))]
    ans = []

    for i in range(len(arr)):
        if i == 0:
            ps[i] = arr[i]
        else:
            ps[i] = ps[i-1] + arr[i]
    for query in queries:
        si = query[0]
        ei = query[1]

        if si == 0:
            ans.append(ps[ei])
        else:
            ans.append(ps[ei] - ps[si-1])
    return ans

def main():
    arr = [3,-1,2,5,6,-3,-1,6]
    queries = [[1,3],[2,5],[1,6],[0,7]]
    ans = getOptimizedQueriesResult(arr,queries)
    print(ans)

main()
    