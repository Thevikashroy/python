#  print all Haspath using list 












# build graph using list(in weighted graph)
# DFS using bulid graph bi-directionl Weight graph 


def buildGraph(edges,n):
    graph = [[] for i in range(n)]

    for i in range(len(edges)):
        edge = edges[i]
        src = edge[0]
        nbr = edge[1]
        wt = edge[2]

        graph[src].append([nbr,wt])
        graph[nbr].append([src,wt])

    return graph





def main():
    edges = [[0,1,2],[1,2,2],[1,3,3],[2,3,3],[3,4,10],[4,5,6],[5,7,3],[4,6,18],[6,7,-5]]
    n = 8
    # src = 0
    # des = 7
    # visited = [0 for i in range(n)]
    # visited[src] = 1
    graph = buildGraph(edges,n)
    print(graph)

main()

