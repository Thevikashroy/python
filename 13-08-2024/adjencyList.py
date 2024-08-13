#  adjency list
#  buildGraph using list ans bidiredted and no self node ,no weighted



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


        # this is another way my point
        # graph[edge[0]].append(edge[1])
        # graph[edge[1]].append(edge[0])
    # return graph




# driver code

def main():
    n = 8
    edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[4,6],[6,7],[5,7]]
    graph = buildGraph(edges,n)
    print(graph)
main()