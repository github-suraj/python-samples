from collections import defaultdict

class Graph(object):
    def __init__(self, edges=list()):
        self._graph = defaultdict(set)
        self.addEdges(edges)
    
    def getGraph(self):
        return dict(self._graph)

    def getNodes(self):
        return list(self._graph.keys())

    def getEdges(self):
        edges = list()
        for start, ends in self._graph.items():
            for end in ends:
                edges.append((start, end))
        return edges

    def addEdges(self, edges):
        if not isinstance(edges, (list, tuple)):
            raise TypeError(f"edges should be an iterable (list/tuple)")
        if edges:
            for edge in edges:
                if not isinstance(edge, (list, tuple)) or len(edge) != 2:
                    raise TypeError(f"an edge should be two value iterable (list/tuple), but got {edge}")
                self.addEdge(*edge)

    def addEdge(self, start, end):
        self._graph[start].add(end)

    def removeEdges(self, edges):
        if not isinstance(edges, (list, tuple)):
            raise TypeError(f"edges should be an iterable (list/tuple)")
        if edges:
            for edge in edges:
                if not isinstance(edge, (list, tuple)) or len(edge) != 2:
                    raise TypeError(f"an edge should be two value iterable (list/tuple), but got {edge}")
                self.removeEdge(*edge)

    def removeEdge(self, start, end):
        if start not in self._graph:
            raise ValueError(f"invalid start node {start}")
        if end not in self._graph[start]:
            raise ValueError(f"invalid edge ({start}-->{end})")
        self._graph[start].remove(end)
        if not self._graph[start]:
            self._graph.pop(start)

    def getPaths(self, start, end, path=list()):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self._graph:
            return list()
        paths = list()
        for node in self._graph[start]:
            if node not in path:
                temp_paths = self.getPaths(node, end, path)
                for p in temp_paths:
                    paths.append(p)
        return paths
        
    def getSortestPath(self, start, end, path=list()):
        path = path + [start]
        if start == end:
            return path
        if start not in self._graph:
            return None
        sortest_path = None
        for node in self._graph[start]:
            if node not in path:
                sp = self.getSortestPath(node, end, path)
                if sortest_path is None or len(sp) < len(sortest_path):
                    sortest_path = sp
        return sortest_path

    def __str__(self):
        return f"Graph({self.getGraph()})"
