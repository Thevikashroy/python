
# Check the all component of given array ,disconnected Graph


def buildGraph(edges,n):
    graph = [[0 for i in range(n)] for j in range(n)]
    for edge in edges:
        src = edge[0]
        des = edge[1]
        graph[src][des] = 1
        graph[des][src] = 1

    return graph



def expandNode(graph,n,src,currComponent,visited):
    nbrs = graph[src]
    for i in range(len(nbrs)):
        if nbrs[i] == 1 and visited[i] == 0:
            visited[i] = 1
            currComponent.append(i)
            expandNode(graph,n,i,currComponent,visited)



def getAllComponents(graph,n):
    visited = [0 for i in range(n)]
    ans = []
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            currComponent = [i]
            expandNode(graph,n,i,currComponent,visited)
            ans.append(currComponent)
    return ans





def main():
    n = 12
    edges = [[0,2],[0,3],[1,3],[4,5],[6,7],[6,8],[8,9],[10,11]]
    src = 0
    graph = buildGraph(edges,n)

    ans = getAllComponents(graph,n)
    print(ans)


main()