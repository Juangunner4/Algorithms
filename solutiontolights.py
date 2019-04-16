
from copy import deepcopy


def make_graph(walls, lights, switches):
    '''Makes bipartite graph given walls, lights, and switches.'''
    graph = LinkedDirectedGraph()
    graph.addVertex('0')  # The source is labeled as '0'
    graph.addVertex('1')  # The sink is labeled as '1'
    for i, v in enumerate(lights):
        graph.addVertex(str(v))
        graph.addEdge('0', str(v), 0)  # lights are connected to the source
    for i, v in enumerate(switches):
        graph.addVertex(str(v))  # switches are connected to the sink
        graph.addEdge(str(v), '1', 0)

    # adapted from: http://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

    # Return true if line segments AB and CD intersect
    def intersect(A, B, C, D):
        return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

    for l in lights:
        for s in switches:
            path = True
            for i, w in enumerate(walls[:-1]):
                next_w = walls[i + 1]
                if intersect(s, l, w, next_w):
                    path = False
                    print('Wall ' + str(w), str(next_w) + ' blocked light ' + str(l) + ' and switch ' + str(s))
                    break
            if path:
                graph.addEdge(str(l), str(s), 0)
    return graph


def find_path(graph, start, stop):
    # print(graph)
    search = breadthFirst(graph, start)
    # print(search)
    search.reverse()
    i = search.index('1')
    skip = False
    path = []
    while True:
        node2 = search[i]
        for index, node1 in enumerate(search[i:]):
            if graph.containsEdge(node1, node2):
                path.append(node1)
                if node1 == '1':
                    path = []
                if node1 == '0':
                    path.reverse()
                    path.append('1')
                    return path
                i = index + i
                skip = True
                break
        if not (skip):
            i += 1


def augment(graph, flow, path):
    # print(graph)
    # print(path)
    # print(flow)
    for i in range(len(path) - 1):

        node1 = path[i]
        node2 = path[i + 1]
        edge = graph.getEdge(node1, node2)
        if graph.containsEdge(node1, node2):
            flow[str(edge)] += 1
        else:
            flow[str(node1) + '>' + str(node2) + ':0'] -= 1
    return flow


def max_flow(graph):
    flow = {}
    for i in graph.edges():
        flow.update({str(i): 0})
    while hasPath(graph, '0', '1'):
        path = find_path(graph, '0', '1')
        flow = augment(graph, flow, path)
        for i in range(len(path) - 1):
            node1 = path[i]
            node2 = path[i + 1]
            graph.addEdge(node2, node1, 0)
            flow[str(graph.getEdge(node2, node1))] = 0
            # print(node1,node2)
            graph.removeEdge(node1, node2)
    return graph, flow


def answer(lights, switches, graph):
    original_g = deepcopy(graph)
    g, flow = max_flow(graph)
    # print(g)
    if len(lights) != len(switches):
        return False
    count = 0
    matches = []
    for key, value in flow.items():
        if value == 1:
            if key[0] == '0' or key[-3] == '1':
                continue
            node1 = key[:key.index('>')]
            node2 = key[key.index('>') + 1:-2]
            if not (original_g.containsEdge(str(node2), str(node1))):
                count += 1
                matches.append([node1, node2])
    if count == len(lights):
        print('Possible matching: ')
        for i in matches:
            print(i)
        return True  # all lights have a path
    print('Certificate:')
    certificate = breadthFirst(g, '0')
    print(certificate[1:])
    return False


walls = [(1, 2), (1, 5), (8, 5), (8, 3), (11, 3), (11, 1),  # FOR FIRST 3 TEST CASES
         (5, 1), (5, 3), (4, 3), (4, 1), (1, 1), (1, 2)]

'''
#TEST 1 TRUE
lights = [(2,4),(2,2),(5,4)]
switches = [(4,4),(6,3),(6,2)]
'''

# TEST 2 FALSE
lights = [(2, 4), (2, 2), (5, 4)]
switches = [(6, 2), (7, 4), (6, 3)]

# TEST 3 FALSE
lights = [(2, 4), (2, 2), (5, 4)]
switches = [(6, 2), (7, 2), (4, 4)]

# walls = [(2, 8), (2, 2), (8, 2), (8, 4), (9, 4), (9, 2), #FOR NEXT 3 TEST CASES
#         (11, 2), (11, 8), (5, 8), (5, 6), (4, 6), (4, 8), (2, 8)]
'''
#True
lights = [(4, 3), (10, 3), (10, 7)]
switches = [(6, 3), (6, 6), (10, 4)]
'''
'''
#True
lights = [(3, 7), (6, 7), (7, 3), (10, 3)]
switches = [(4, 3), (7, 5), (8, 7), (10, 5)]

#False
lights = [(3, 7), (6, 7), (7, 3), (10, 3)]
switches = [(7, 5), (8, 6), (8, 7), (10, 7)]
'''
answer(lights, switches, make_graph(walls, lights, switches))