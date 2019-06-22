"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        if not vertex in self.vertices:
            self.vertices[vertex] = set()
        else:
            print(f"{vertex} vertex already exists")
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print(f"Either {v1}, {v2}, or both vertices do not exist")

    def bft(self, starting_vertex):
        print("BFT")
        visited = set()
        q = Queue()
        q.enqueue(starting_vertex)
        while(q.size() > 0):
            v = q.dequeue()
            if(v not in visited):
                visited.add(v)
                print(v)
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
                
    def dft(self, starting_vertex):
        print("DFT")
        visited = set()
        s = Stack()
        s.push(starting_vertex)

        while(s.size() > 0):
            v = s.pop()
            if(v not in visited):
                visited.add(v)
                print(v)
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        

    def dft_recursive(self, starting_vertex):
        print("Recursive DFT")
        visited = self._dftr_loop(starting_vertex)
        for v in visited:
            print(v)

    def _dftr_loop(self, vertex, visited=set()):
        if(vertex in visited):
            return visited
        visited.add(vertex)
        for neighbor in self.vertices[vertex]:
            self._dftr_loop(neighbor, visited)
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        print("BFS")
        visited = set()
        q = Queue()
        q.enqueue([1])
        paths = {}
        while(q.size() > 0):
            path = q.dequeue()
            v = path[-1]
            if(v == destination_vertex):
                length = len(path)
                if(length in paths):
                    paths[length].append(path)
                else:
                    paths[length] = [path]
            elif(not v in visited):
                visited.add(v)
                for neighbor in self.vertices[v]:
                    q.enqueue([*path, neighbor])
        smallest = min(paths.keys())
        return None if len(paths[smallest]) == 0 else paths[smallest] if len(paths[smallest]) > 1 else paths[smallest][0]

        
    def dfs(self, starting_vertex, destination_vertex):
        print("BFS")
        visited = set()
        s = Stack()
        s.push([1])
        paths = {}
        while(s.size() > 0):
            path = s.pop()
            v = path[-1]
            if(v == destination_vertex):
                length = len(path)
                if(length in paths):
                    paths[length].append(path)
                else:
                    paths[length] = [path]
            elif(not v in visited):
                visited.add(v)
                for neighbor in self.vertices[v]:
                    s.push([*path, neighbor])
        smallest = min(paths.keys())
        return None if len(paths[smallest]) == 0 else paths[smallest] if len(paths[smallest]) > 1 else paths[smallest][0]





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
