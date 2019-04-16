# visits all the nodes of a graph (connected component) using BFS
def BFS(graph, s):

    visited = []     # List that stores nodes visited

    queue = [s]      # Keeps all the nodes that another node can connect with and start with s

    # keep looping until there are nodes still to be checked
    while queue:
        node = queue.pop(0)      # current node
        print(node, 'node now')
        if node not in visited:  # if the start node is not in the visited list add it
            visited.append(node)
            print(visited, 'nodes visited')
            newnode = graph[node]

            print(newnode, 'nodes',node, 'can visit')
            for othernodes in newnode:
                queue.append(othernodes)  # Stores the nodes in the list
                print(queue, 'queue')
    return 'End' in visited
print(BFS(edgest,'start'))
