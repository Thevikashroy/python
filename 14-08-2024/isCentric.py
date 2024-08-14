#  find the graph is centric or not


def findCenterNode(graph):
    n = len(graph)
    for i in range(len(graph)):
        nbrs = graph[i]
        if len(nbrs) == n - 1:
            return i
    return -1

def isCentric(graph):
  
    n = len(graph)
    centerNode = findCenterNode(graph)
    
    
    if centerNode == -1:
        return False
    
    # Check if all nodes are connected to the center node
    for i, nbrs in enumerate(graph):
        if i != centerNode and centerNode not in nbrs:
            return False
            
    return True

def main():
    # Define the graph as an adjacency list
    edges = [[0,1], [0,2], [0,3], [0,4]]
    n = 4
    
    # Check if the graph is centric
    print(isCentric(edges))  

main()

