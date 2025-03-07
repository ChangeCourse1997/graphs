import streamlit as st
dfs = """
Depth-First Search (DFS) 
•	Input:
o	A simple graph in adjacency list format
o	A starting vertex
	This is optional. If not provided, DFS will start from an arbitrary location.
	This is accomplished through adjacency list ordering, which we assume takes place when you provide a starting vertex.
•	Internal (not accessible after run):
o	visited[] - A list containing whether the indexed vertex was touched by DFS.
	All entries of this list will always be set to true when DFS completes.
	This is populated by Explore, an internal subroutine of DFS.
•	Output:
o	ccnum[] - A list containing the connected component number of the indexed vertex.
	Vertices reachable from the starting vertex will have a connected component number of 1.
•	
o	prev[] - A list containing the parent vertex of the indexed vertex, which can be used to create a path from the starting vertex to any reachable vertex.
	Unreachable vertices and the starting vertex have a parent of nil.
o	pre[] - A list containing the pre-visit number for the indexed vertex.
o	post[] - A list containing the post-visit number for the indexed vertex.
•	Runtime:
o	O(n + m)
"""
topological_sort = """
Topological Sort 
•	Input:
o	A simple, directed, acyclic graph in adjacency list format
•	Output:
o	order[] - A list of vertices, sorted in topological ordering from source to sink.
	Note: This output is indexed numerically rather than by vertex.
o	All outputs from the run of Depth-First Search (DFS) are also available to you.
•	Runtime:
o	O(n + m)
"""
scc = """
Strongly Connected Components (SCC) 
•	Input:
o	A simple, directed graph in adjacency list format
•	Output:
o	G_SCC = (V_SCC, E_SCC) - The strongly connected components metagraph, provided in adjacency list format.
	By construction, the metagraph is a DAG with vertices sorted from sink to source
	This ordering is known as reverse topological ordering.
o	All outputs from the final run of Depth-First Search (DFS) are also available to you.
	This data is used to connect entities in the metagraph to the original input graph.
	For example, the first vertex in V_SCC represents all vertices with ccnum[v] = 1 from the DFS outputs from the original input graph.
•	Runtime:
•	
o	O(n + m)
"""
bfs = """
Breadth-First Search (BFS) 
•	Input:
o	A simple graph in adjacency list format
o	A starting vertex
•	Output:
o	dist[] - A list containing the unweighted distance from the starting vertex to the indexed vertex for all vertices in the graph.
	Unreachable vertices have a distance of inf.
o	prev[] - A list containing the parent vertex of the indexed vertex, which can be used to create a path from the starting vertex to any reachable vertex.
	Unreachable vertices and the starting vertex have a parent of nil.
•	Runtime:
o	O(n + m)
"""
dikstras = """
Dijkstra's 
•	Input:
o	A simple graph in adjacency list format
o	A starting vertex
o	A list of non-negative edge weights
•	Output:
•	
o	dist[] - A list containing the weighted distance from the starting vertex to the indexed vertex for all vertices in the graph.
	Unreachable vertices have a distance of inf.
o	prev[] - A list containing the parent vertex of the indexed vertex, which can be used to create a path from the starting vertex to any reachable vertex.
	Unreachable vertices and the starting vertex have a parent of nil.
•	Runtime:
o	O((n + m) log n)
"""
bellman = """
Bellman-Ford (BF) 
•	Input:
o	A simple graph in adjacency list format
o	A starting vertex
o	A list of edge weights
•	Output:
•	
o	dist[] - A list containing the weighted distance from the starting vertex to the indexed vertex for all vertices in the graph.
	Unreachable vertices have a distance of inf.
	Values are based on the n-1 th iteration.
o	prev[] - A list containing the parent vertex of the indexed vertex, which can be used to create a path from the starting vertex to any reachable vertex.
	Unreachable vertices and the starting vertex have a parent of nil.
o	iter[][] - A 2-dimensional list containing the first indexed iteration's shortest path from the starting vertex to the second indexed vertex.
	For example, iter[3][v] contains the distance from the starting vertex to v at the end of the 3rd iteration.
	This table contains iterations 0 through n.
•	Runtime:
o	O(nm)
"""
floyd = """
Floyd-Warshall (FW)
•	Input:
o	A simple graph in adjacency list format
o	A list of edge weights
•	Output:
•	
o	dist[][] - A 2-dimensional list containing the weighted distance from the first indexed vertex to the second indexed vertex.
	For example, dist[u][v] would contain the shortest path from vertex u to vertex v.
	Unreachable vertex pairs have a distance of inf.
	Values are based on the nth iteration.
o	iter[][][] - A 3-dimensional list containing the first indexed iteration's shortest path from the second indexed vertex to the third indexed vertex.
	For example, iter[3][u][v] contains the distance from u to v at the end of the 3rd iteration.
	This table contains iterations 0 through n.
•	Runtime:
o	O(n^3)
"""
kruskal = """
Kruskal's 
•	Input:
o	A simple, connected, undirected graph in adjacency list format
o	A list of edge weights
•	Output:
o	edges[] - A list of n-1 edges that represent a minimum spanning tree for the input graph.
•	Runtime:
o	O(m log n)
"""
prim = """
Prim's 
•	Input:
o	A simple, connected, undirected graph in adjacency list format
o	A list of edge weights
•	Output:
•	
o	prev[] - A list containing the parent vertex of the indexed vertex, which represent the connecting edges of a minimum spanning tree for the input graph.
	The starting vertex is chosen arbitrarily and has a parent of nil.
•	Runtime:
o	O(m log n)
"""
fulkerson = """
Ford-Fulkerson (FF) 
•	Input:
o	A simple, connected, directed graph in adjacency list format
o	A list of positive, integer edge capacities
o	A starting source vertex
o	A terminating sink vertex 
•	Output:
o	flow[] - A list of edges representing the amount capacity used per each indexed edge such that the flow is maximized from the starting vertex to the terminating vertex.
o	C - The value of the maximum flow from the starting vertex to the terminating vertex.
•	Runtime:
o	O(mC)
"""
edmond = """
Edmonds-Karp (EK)
•	Input:
o	A simple, connected, directed graph in adjacency list format
o	A list of positive edge capacities
o	A starting source vertex
o	A terminating sink vertex 
•	Output:
o	flow[] - A list of edges representing the amount capacity used per each indexed edge such that the flow is maximized from the starting vertex to the terminating vertex.
o	C - The value of the maximum flow from the starting vertex to the terminating vertex.
•	Runtime:
o	O(nm^2)
"""
sat = """
2-SAT 
•	Input:
o	A Boolean formula in conjunctive normal form such that each clause contains at most 2 literals.
	This formula is backed by a list of n variables, representing at most 2n literals and m clauses.
•	Output:
o	assignments[] - A list indexable by the variables that back the original input formula containing whether that variable is set to true or false.
	If the input is not satisfiable, this will instead return "NO"
o	All outputs from the Strongly Connected Components (SCC) run are also available to you.
•	Runtime:
o	O(n + m)
"""
if __name__ =='__main__':
    st.title('black box')
    for algo in [dfs,topological_sort,scc,bfs,dikstras,bellman,floyd,kruskal,prim,fulkerson,edmond,sat]:
        st.code(algo,language='python')