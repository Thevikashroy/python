
# buildhashpath graph using list according to bi-directed graph

def hasPath(graph,n,src,des,visited):
    if src == des:
        return True
    nbrs = graph[src]

    for nbr in  nbrs:
        currentNbr = nbr[1]
        if visited[currentNbr] == 0:
            visited[currentNbr] = 1
            ans = hasPath(graph,n,currentNbr,des,visited)
            if ans == True:
                return True
    return False





def buildGraph(edges,n):
    graph = [[] for i in range(n)]
    for i in range(len(edges)):
    
        edge = edges[i]
        src1 = edge[0]
        src2 = edge[1]

        des1 = edge
        des2 = edge[::-1]

        graph[src1].append(des1)
        graph[src2].append(des2)
    
    return graph






def main():
    n = 8
    edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[4,6],[6,7],[5,7]]
    graph = buildGraph(edges,n)
    src = 0
    des = 7
    visited = [0 for i in range(n)]
    visited[src] = 1
    
    ans = hasPath(graph,n,src,des,visited)
    print(ans)

main()  