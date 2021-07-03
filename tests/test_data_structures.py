import pytest
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.graph import Graph
from data_structures.linked_list import LinkedList
from data_structures.hash_table import HashTable
from data_structures.general_tree import Tree
from data_structures.binary_search_tree import BinarySearchTree

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

def test_linked_list(capsys):
    ll = LinkedList()
    assert ll.isEmpty() == True, "Test Failed"
    assert len(ll) == 0, "Test Failed"
    assert ll.getElements() == [], "Test Failed"
    print(ll)
    assert capsys.readouterr().out.rstrip() == f"LinkedList([])", "Test Failed"
    with pytest.raises(IndexError) as err:
        ll.pop()
        assert err.exception == "Popping an emply list", "Test Failed"
    with pytest.raises(IndexError) as err:
        ll.popleft()
        assert err.exception == "Popping an emply list", "Test Failed"
    with pytest.raises(ValueError) as err:
        ll.remove(5)
        assert err.exception == "5 not in the list", "Test Failed"

    data = list(range(1, 5))
    ll = LinkedList(data)
    assert ll.isEmpty() == False, "Test Failed"
    assert len(ll) == 4, "Test Failed"
    assert ll.getElements() == data, "Test Failed"
    print(ll)
    assert capsys.readouterr().out.rstrip() == f"LinkedList({[1, 2, 3, 4]})", "Test Failed"
    ll.extendleft(data)
    assert len(ll) == 8, "Test Failed"
    print(ll)
    assert capsys.readouterr().out.rstrip() == f"LinkedList({[4, 3, 2, 1, 1, 2, 3, 4]})", "Test Failed"
    assert ll.pop() == 4, "Test Failed"
    assert ll.popleft() == 4, "Test Failed"
    assert ll.getElements() == [3, 2, 1, 1, 2, 3], "Test Failed"
    with pytest.raises(IndexError) as err:
        ll.insert(6, -1)
        assert err.exception == "Index out of range", "Test Failed"
    ll.insert(0, 4)
    assert ll.getElements() == [4, 3, 2, 1, 1, 2, 3], "Test Failed"
    with pytest.raises(ValueError) as err:
        ll.insert_after_value(5, 6)
        assert err.exception == "5 not in the list", "Test Failed"
    ll.append(5)
    assert ll.getElements() == [4, 3, 2, 1, 1, 2, 3, 5], "Test Failed"
    ll.insert_after_value(5, 6)
    assert len(ll) == 9, "Test Failed"
    print(ll)
    assert capsys.readouterr().out.rstrip() == f"LinkedList({[4, 3, 2, 1, 1, 2, 3, 5, 6]})", "Test Failed"
    ll.remove(2)
    assert len(ll) == 8, "Test Failed"
    assert ll.getElements() == [4, 3, 1, 1, 2, 3, 5, 6], "Test Failed"
    with pytest.raises(ValueError) as err:
        ll.remove(7)
        assert err.exception == "7 not in the list", "Test Failed"
    ll.remove_at_index(5)
    assert len(ll) == 7, "Test Failed"
    print(ll)
    assert capsys.readouterr().out.rstrip() == f"LinkedList({[4, 3, 1, 1, 2, 5, 6]})", "Test Failed"
    with pytest.raises(IndexError) as err:
        ll.remove_at_index(7)
        assert err.exception == "Index out of range", "Test Failed"

def test_hash_table(capsys):
    data = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ht = HashTable()
    assert ht.isEmpty() == True, "Test Failed"
    assert len(ht) == 0, "Test Failed"
    ht['Jan'] = 1
    print(ht)
    assert capsys.readouterr().out.rstrip() == f"HashTable([('Jan', 1)])", "Test Failed"
    for idx, month in enumerate(data[1:], start=2):
        ht[month] = idx
    assert ht.isEmpty() == False, "Test Failed"
    assert sorted(ht.values()) == list(range(1, 13)), "Test Failed"
    assert sorted(ht.keys()) == sorted(data), "Test Failed"
    assert dict(ht.items()) == dict([(month, idx) for idx, month in enumerate(data, start=1)]), "Test Failed"
    assert len(ht) == 12, "Test Failed"
    assert ht['May'] == 5, "Test Failed"
    del ht['Dec']
    assert dict(ht.items()) == dict([(month, idx) for idx, month in enumerate(data[:-1], start=1)]), "Test Failed"
    assert len(ht) == 11, "Test Failed"
    for idx, month in enumerate(data[:-1], start=1):
        del ht[month]
        assert len(ht) == 11 - idx, "Test Failed"
    assert ht.isEmpty() == True, "Test Failed"
    assert len(ht) == 0, "Test Failed"

def test_general_tree(capsys):
    car = Tree('Car')
    car.add_child(Tree('Audi'))
    car.add_child(Tree('BMW'))

    bike = Tree('Bike')
    bike.add_child(Tree('Bullet'))
    bike.add_child(Tree('Rajdoot'))

    root = Tree('Vehical')
    root.add_child(car)
    root.add_child(bike)
    root.print_tree()
    expected = ['Vehical', '   |--Car', '      |--Audi', '      |--BMW', '   |--Bike', '      |--Bullet', '      |--Rajdoot']
    assert capsys.readouterr().out.splitlines() == expected, "Test Failed"

def test_binary_search_tree(capsys):
    arr = [3, 1, 2, 0, 5, 6, 4]
    root = BinarySearchTree(arr[0])
    assert len(root) == 1, "Test Failed"
    for idx, ele in enumerate(arr[1:], start=1):
        root.insert(ele)
        assert len(root) == idx + 1, "Test Failed"
    print(root)
    assert capsys.readouterr().out.rstrip() == 'BinarySearchTree([0, 1, 2, 3, 4, 5, 6])', "Test Failed"
    assert root.isEmpty() == False, "Test Failed"
    assert root.inorderTree() == [0, 1, 2, 3, 4, 5, 6], "Test Failed"
    assert root.preorderTree() == [3, 1, 0, 2, 5, 4, 6], "Test Failed"
    assert root.postorderTree() == [0, 2, 1, 4, 6, 5, 3], "Test Failed"
    assert root.findMin() == 0, "Test Failed"
    assert root.findMax() == 6, "Test Failed"
    assert root.treeSum() == 21, "Test Failed"
    assert root.search(6) == True, "Test Failed"
    assert root.search(8) == False, "Test Failed"
    for i in range(7):
        root = root.delete(i)
        if root:
            print(root)
            assert root.inorderTree() == sorted(arr)[i+1:], "Test Failed"
            assert len(root) == len(arr) - i - 1, "Test Failed"
