from collections import deque

class Graph:
    def __init__(self):
        self.graph={}


    def addEdge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        self.graph[u].append(v)        

    def BFS(self,start):
        graph=self.fetch_graph()
        visited = {node: False for node in graph.keys()}

        queue=[start]
        visited[start]=True
        
        while queue:

            start=queue.pop(0)
            print(start,end=" ")

            for i in graph[start]:
                if not visited[i]:
                    queue.append(i)
                    visited[i]=True
    
    def DFS(self,start):
        graph=self.fetch_graph()
        visited=set() 

        stack=[start]
        dfs_order=[]

        while stack:
            node=stack.pop()
            if node not in visited:
                visited.add(node)
                dfs_order.append(node)

                for neighbor in reversed(graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return dfs_order

    def fetch_graph(self):
        return self.graph.copy()
    
    def clear_graph(self):
        self.graph={}
    
if __name__ == '__main__':

    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print(g.fetch_graph())
    print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
    
    g.BFS(2)

    print("Following is Depth First Traversal"
        " (starting from vertex 2)")
    print(g.DFS(0))
