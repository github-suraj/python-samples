from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.graph import Graph

def test_stack(capsys):
    s = Stack()
    assert s.isEmpty() == True, "Test Failed"
    assert s.getSize() == 0, "Test Failed"
    for i in range(1, 10):
        s.push(i)
    assert s.isEmpty() == False, "Test Failed"
    assert s.getSize() == 9, "Test Failed"
    assert s.peak() == 9, "Test Failed"
    assert s.getElements() == list(range(9, 0, -1)), "Test Failed"
    print(s)
    assert capsys.readouterr().out.rstrip() == f"Stack({list(range(9, 0, -1))})", "Test Failed"
    assert s.pop() == 9, "Test Failed"
    assert s.pop() == 8, "Test Failed"
    assert s.getSize() == 7, "Test Failed"
    assert s.peak() == 7, "Test Failed"
    assert s.getElements() == list(range(7, 0, -1)), "Test Failed"
    print(s)
    assert capsys.readouterr().out.rstrip() == f"Stack({list(range(7, 0, -1))})", "Test Failed"
    for i in range(7, 0, -1):
        assert s.pop() == i, "Test Failed"
    assert s.isEmpty() == True, "Test Failed"
    assert s.getSize() == 0, "Test Failed"
    assert s.getElements() == [], "Test Failed"
    print(s)
    assert capsys.readouterr().out.rstrip() == f"Stack([])", "Test Failed"

def test_queue(capsys):
    q = Queue()
    assert q.isEmpty() == True, "Test Failed"
    assert q.getSize() == 0, "Test Failed"
    for i in range(1, 10):
        q.enQueue(i)
    assert q.isEmpty() == False, "Test Failed"
    assert q.getSize() == 9, "Test Failed"
    assert q.first() == 1, "Test Failed"
    assert q.getElements() == list(range(1, 10)), "Test Failed"
    print(q)
    assert capsys.readouterr().out.rstrip() == f"Queue({list(range(1, 10))})", "Test Failed"
    assert q.deQueue() == 1, "Test Failed"
    assert q.deQueue() == 2, "Test Failed"
    assert q.getSize() == 7, "Test Failed"
    assert q.first() == 3, "Test Failed"
    assert q.getElements() == list(range(3, 10)), "Test Failed"
    print(q)
    assert capsys.readouterr().out.rstrip() == f"Queue({list(range(3, 10))})", "Test Failed"
    for i in range(3, 10):
        assert q.deQueue() == i, "Test Failed"
    assert q.isEmpty() == True, "Test Failed"
    assert q.getSize() == 0, "Test Failed"
    assert q.getElements() == [], "Test Failed"
    print(q)
    assert capsys.readouterr().out.rstrip() == f"Queue([])", "Test Failed"

def test_graph(capsys):
    data = [('A', 'B'), ('A', 'C'), ('C', 'D')]
    data_dict_1 = {'A': {'B', 'C'}, 'C': {'D'}}
    g = Graph(data)
    assert g.getGraph() == data_dict_1, "Test Failed"
    print(g)
    assert capsys.readouterr().out.rstrip() == f"Graph({data_dict_1})", "Test Failed"

    edges = g.getEdges()
    for edge in edges:
        assert (edge in data) == True, "Test Failed"

    data_add = [('B', 'C'), ('B', 'D')]
    g.addEdges(data_add)
    data_dict_2 = {'A': {'B', 'C'}, 'C': {'D'}, 'B': {'C', 'D'}}
    assert g.getNodes() == ['A', 'C', 'B'], "Test Failed"
    assert g.getGraph() == data_dict_2, "Test Failed"
    print(g)
    assert capsys.readouterr().out.rstrip() == f"Graph({data_dict_2})", "Test Failed"

    edges = g.getEdges()
    for edge in edges:
        assert (edge in data + data_add) == True, "Test Failed"
        
    paths = g.getPaths('A', 'D')
    expected = [['A', 'B', 'D'], ['A', 'C', 'D'], ['A', 'B', 'C', 'D']]
    for path in paths:
        assert (path in expected) == True, "Test Failed"

    assert (g.getSortestPath('A', 'D') in expected[:2]) == True, "Test Failed"

    g.removeEdges(data_add)
    assert g.getGraph() == data_dict_1, "Test Failed"
    print(g)
    assert capsys.readouterr().out.rstrip() == f"Graph({data_dict_1})", "Test Failed"

    edges = g.getEdges()
    for edge in edges:
        assert (edge in data) == True, "Test Failed"
