from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other Attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False
        self.color = ""

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.graph = {} # dictionary that holds all the vertices
        # opens the file to read
        try:
            with open(filename, "rt") as f:
                for line in f:
                    s_line = line.split() # takes each line and splits it into elements
                # each element and the second both are added as vertices
                    for i in range(0, len(s_line) - 1, 2):
                        self.add_vertex(s_line[i])
                        self.add_vertex(s_line[i + 1])
                        self.add_edge(s_line[i], s_line[i + 1]) # add each other to adjacent list

         # print(self.graph)
         # This method should call add_vertex and add_edge!!!
        finally:
            f.close()

    def add_vertex(self, key):
        # Should be called by init
        '''Add vertex to graph only if the vertex is not already in the graph.'''
        if key not in self.graph:
            self.graph[key] = Vertex(key)

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph[v1].adjacent_to.append(v2)
        self.graph[v2].adjacent_to.append(v1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        if key not in self.graph:
            return None

        # returns the object with the id
        return self.graph[key]

    def get_vertices(self):
        '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
        ids = []
        for key in self.graph:
            ids.append(self.graph[key].id)

        return sorted(ids)

    def conn_components(self): 
        '''Return a Python list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending alphabetical order) in the connected component represented by that list.
           The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        #This method MUST use Depth First Search logic!
        con_comp_lst = []
        for vertex in self.graph:
            if self.graph[vertex].visited is False:
                lst = self.depth_first_search(self.graph[vertex])
                con_comp_lst.append(lst)

        for vertex in self.graph:
            #reset everything back to the way it was
            self.graph[vertex].visited = False

        return sorted(con_comp_lst)

    def depth_first_search(self, vertex):
        # helper that goes through the graph vertex by vertex
        lst =[]
        dfs_vertices = Stack(30000)
        # for the very first vertex
        lst.append(vertex.id)
        vertex.visited = True
        # push all the adjacent vertices of the first vertex into the stack
        for adj_vertex in vertex.adjacent_to:
            dfs_vertices.push(self.graph[adj_vertex])

        while not dfs_vertices.is_empty():
            current_vertex = dfs_vertices.pop()
            # if the vertex has not been visited, put it into the final list
            if current_vertex.visited is False:
                lst.append(current_vertex.id)
                # then we add its adjacent vertices into the stack
                for adj_vertex in current_vertex.adjacent_to:
                    dfs_vertices.push(self.graph[adj_vertex])
                current_vertex.visited = True

        return sorted(lst)


    def is_bipartite(self):
        '''Return True if the graph is bipartite, False otherwise.'''
        #This method MUST use Breadth First Search logic!
        boolean_value = True
        for vertex in self.graph:
            if self.breath_first_search(self.graph[vertex]) is False: # makes a graph of each vertex as the root
                boolean_value = False
                break
        for vertex in self.graph:
            self.graph[vertex].visited = False

        return boolean_value

    def breath_first_search(self, vertex):
        bfs_queue = Queue(10 + len(self.graph))
        bfs_queue.enqueue(vertex)
        vertex.visited = True
        color = "black"
        vertex.color = color

        while not bfs_queue.is_empty():
            current_vertex = bfs_queue.dequeue()
            for adj_verts in current_vertex.adjacent_to:
                if self.graph[adj_verts].visited is False:
                    # enqueue all the possible adjacent vertices to the current vertex
                    bfs_queue.enqueue(self.graph[adj_verts])

                    # each one that is looked through has been visited
                    self.graph[adj_verts].visited = True

                    color = "white" if current_vertex.color == "black" else "black"
                    # the color is white if the original vertex's color was the other
                    # and vice versa
                    self.graph[adj_verts].color = color
                    for vertices in self.graph[adj_verts].adjacent_to:
                        if self.graph[adj_verts].color == self.graph[vertices].color:
                            return False
        return True


