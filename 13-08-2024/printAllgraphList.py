

# def printAllPath(graph,src,des,visited,psf):
#     if src==des:
#         print(psf)
#         return
#     nbrs = graph[src]


#     for i in range(len(nbrs)):
#         if nbrs[i] == 1:
#             if visited[i] == 0:
#                 visited[i] = 1
#                 printAllPath(graph,i,des,visited,psf + str(i) + "->")
#                 visited[i] = 0
#     return False








# def buildGraph(edges,n):
#     graph = [[] for i in range(n)]
#     for i in range(len(edges)):
    
#         edge = edges[i]
#         src1 = edge[0]
#         src2 = edge[1]

#         des1 = edge
#         des2 = edge[::-1]

#         graph[src1].append(des1)
#         graph[src2].append(des2)
    
#     return graph






# def main():
#     n = 8
#     edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[4,6],[6,7],[5,7]]
#     graph = buildGraph(edges,n)
#     src = 0
#     des = 7
#     visited = [0 for i in range(n)]
#     visited[src] = 1   
#     printAllPath(graph,src,des,visited,str(src))


# main() 


def printAllPath(graph, src, des, visited, psf):
    # Base case: if source is the destination, print the path
    if src == des:
        print(psf + str(des))
        return
    
    # Get neighbors of the source node
    nbrs = graph[src]
    
    # Explore each neighbor
    for neighbor in nbrs:
        if not visited[neighbor]:
            visited[neighbor] = True
            printAllPath(graph, neighbor, des, visited, psf + str(src) + "->")
            visited[neighbor] = False  # Backtrack

def buildGraph(edges, n):
    # Initialize adjacency list
    graph = [[] for i in range(n)]
    for edge in edges:
        src, des = edge
        graph[src].append(des)
        graph[des].append(src)  # Since the graph is undirected
    return graph

def main():
    n = 8  # Number of nodes
    edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5],[4,6],[6,7],[5,7]]
    graph = buildGraph(edges, n)
    src = 0
    des = 7
    visited = [False] * n
    visited[src] = True  # Mark the source as visited
    printAllPath(graph, src, des, visited, "")

main()
