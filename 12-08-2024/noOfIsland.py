





def countIsland(edges,row,col):
    count = 0
    visited = [[0 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            if visited[i][j] == 1 and m[i][j] == 0:
                count += 1







def main():
    edges = [[0, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 0, 0, 0, 0],
             [1, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 0, 1, 1],
             [1, 1, 0, 0, 1, 0, 1],
             [1, 1, 1, 1, 1, 0, 0],
             [0, 0, 0, 1, 1, 1, 1],]
    row = len(edges)
    col = len(edges[0])
    graph = buildGraph(row,col,edges)
    print("Total no of island",graph.countIsland)

main()

