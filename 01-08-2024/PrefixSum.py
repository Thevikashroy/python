# si = start index
# ei = end index


def getQueriesResult(arr,queries):
    ans = []
    for i in range(len(queries)):
        query = queries[i]
        si = query[0]
        ei = query[1]
        cs = sum(arr[si:ei+1])
        ans.append(cs)
    return ans



def main():
    arr = [3,-1,2,5,6,-3,-1,6]
    queries = [[1,3],[2,5],[1,6],[0,7]]
    ans = getQueriesResult(arr,queries)
    print(ans)
main()