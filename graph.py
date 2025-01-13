
from queue import deque

class graph_with_adjacency_list():
    def __init__(self):
        self.V = []
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex in self.V:
            print("Vertex is already present")
        else:
            self.V.append(vertex)
            self.adj_list[vertex] = []

    def add_edge(self, source, destination, weight=0):
        if source not in self.V or destination not in self.V:
            print("One or more vertices not present")
        else:
            self.adj_list[source].append((destination, weight))
            #self.adj_list[destination].append((source, weight)) #un-comment if this needs to be bi-directional

    def display_graph(self):
        for vertex in self.V:
            print("Vertex: {}".format(vertex))

        for vertex, edge in self.adj_list.items():
            print("{} --> {}".format(vertex, edge))

    def graph_bfs_search(self, item):
        visited = set()
        queue = deque()
        graph_start = self.V[0]

        visited.add(graph_start)
        queue.append(graph_start)

        while queue:
            vertex = queue.popleft()
            print(vertex)
            for vtx in self.adj_list[vertex]:
                if vtx[0] == item:
                    return "Item " + item + " found adjacent to "  + vertex
                if vtx[0] not in queue  and vtx[0] not in visited:
                    queue.append(vtx[0]) 
                    visited.add(vtx[0])

    def graph_dfs_search(self, item):
        visited = set()
        stack = []
        graph_start = self.V[0]

        visited.add(graph_start)
        stack.append(graph_start)

        while stack:
            vertex = stack.pop()
            print(vertex)
            for vtx in self.adj_list[vertex]:
                if vtx[0] == item:
                    return "Item " + item + " found adjacent to "  + vertex
                if vtx[0] not in stack  and vtx[0] not in visited:
                    stack.append(vtx[0]) 
                    visited.add(vtx[0])

graph = graph_with_adjacency_list()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")
graph.add_vertex("H")
graph.add_vertex("I")
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "D", 1)
graph.add_edge("B", "E", 3)
graph.add_edge("B", "F", 2)
graph.add_edge("C", "G", 4)
graph.add_edge("F", "H")
graph.add_edge("G", "I")
graph.display_graph()
result1 = graph.graph_bfs_search("F")
result2 = graph.graph_dfs_search("I")
print(result1, result2)