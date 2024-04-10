from sys import argv
from stack_array import *

class Vertex:
    def __init__(self):
        '''Add whatever parameters/attributes are needed'''
        self.adjacent_list = []
        self.in_degree = 0

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * one vertex per line in topologically sorted order.
    *
    * Raises a ValueError ]if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message
    *     "input contains a cycle"'''
    vertex_list = {}
    t_sorted = ""

    if len(vertices) == 0:
        raise ValueError("input contains no edges")

    if len(vertices) % 2 != 0:
        raise ValueError("input contains an odd number of tokens")

    for i in range(0, len(vertices) - 1, 2):

        if vertices[i] in vertex_list:
            vertex_list[vertices[i]].adjacent_list.append(vertices[i + 1])
        else:
            vertex_list[vertices[i]] = Vertex()
            vertex_list[vertices[i]].adjacent_list.append(vertices[i + 1])

        if vertices[i + 1] in vertex_list:
            vertex_list[vertices[i + 1]].in_degree += 1
        else:
            vertex_list[vertices[i + 1]] = Vertex()
            vertex_list[vertices[i + 1]].in_degree += 1

    stack = Stack(len(vertices))

    # iterating through the dictionary; if in_degrees is 0 push it
    for item in vertex_list:
        if vertex_list[item].in_degree == 0:
            stack.push(item)

    # cycle would represent the number of times
    # that we pop something from the stack, and therefore equal the number of things in our dictionary
    cycle = 0
    while not stack.is_empty():
        vert = stack.pop() # pop the vertex with 0 in_degrees
        t_sorted += vert + "\n" # adding to the sorted list of vertices
        adj_verts = vertex_list[vert].adjacent_list # reference the adjacent list of popped vertex

        # for each adjacent vertex, we subtract 1 from their degrees because we are taking that vertex out
        for i in range(len(adj_verts)):
            vertex_list[adj_verts[i]].in_degree -= 1
            # if the degree reaches 0 we push it onto the stack
            if vertex_list[adj_verts[i]].in_degree == 0:
                stack.push(adj_verts[i])

        cycle += 1

    # the count would be less than the length of the vertex list if there is a cycle
    if cycle != len(vertex_list):
        raise ValueError("input contains a cycle")

    return t_sorted

    # after we finish creating the list, begin sorting
    # push the in degree of 0s onto the stack, and push the vertices in the order they were encountered in
    # while the stack is not empty
    # pop and output a vertex
    # reduce the in degree of all vertices that were adjacent to the popped vertex
    # push the vertex if reducing the in_degree results in 0


# 100% Code coverage NOT required
def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG.  Use this code 
       if you want to run tests on a file with a list of edges'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)
    
if __name__ == '__main__': 
    main()
