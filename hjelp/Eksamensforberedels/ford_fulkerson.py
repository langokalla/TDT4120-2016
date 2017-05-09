
class Edge(object):

    def __init__(self, source, sink, capacity):
        self.source = source
        self.sink = sink
        self.capacity = capacity

    def __repr__(self):
        return '%s->%s:%s' % (self.source, self.sink, self.capacity)


class FlowNetwork(object):

    def __init__(self):
        self.adj = {}
        self.flow = {}

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def get_edges(self, vertex):
        return self.adj[vertex]

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError('u == v')
        edge = Edge(u, v, w)
        redge = Edge(v, u, 0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0

    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_path(edge.sink, sink, path + [edge])
                if result is not None:
                    return result

    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path is not None:
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))


g = FlowNetwork()
[g.add_vertex(v) for v in 'sopqrt']
"""
g.add_edge('a', 'b', 3)
g.add_edge('a', 'd', 3)
g.add_edge('d', 'f', 6)
g.add_edge('c', 'a', 3)
g.add_edge('c', 'd', 1)
g.add_edge('d', 'e', 2)
g.add_edge('f', 'g', 9)
g.add_edge('b', 'c', 4)
g.add_edge('c', 'e', 2)
g.add_edge('e', 'b', 1)
g.add_edge('e', 'g', 1)

mf = g.max_flow('a', 'g')
print('Max flow:', mf)
"""
g.add_edge('s', 'o', 3)
g.add_edge('s', 'p', 3)
g.add_edge('o', 'p', 2)
g.add_edge('o', 'q', 3)
g.add_edge('p', 'r', 2)
g.add_edge('r', 't', 3)
g.add_edge('q', 'r', 4)
g.add_edge('q', 't', 2)
print(g.max_flow('s', 't'))
