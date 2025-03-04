import streamlit as st

class DFS:
    def __init__(self,nodes,edges):
        self.nodes = nodes
        self.edges = edges
        self.visited = set()
        self.clock = 1
        self.pre = {}
        self.post = {}
        self.scc = {}
        self.explored = set()

    def explore(self,node):
        self.visited.add(node)
        self.pre[node] = self.clock
        self.clock += 1
        for neighbor in self.edges[node]:
            if neighbor not in self.visited:
                self.explore(neighbor)
        self.post[node] = self.clock
        self.clock+=1

    def run_DFS(self):
        for node in self.nodes:
            if node not in self.visited:
                self.explore(node)
        return self.pre,self.post
    
    def reverse(self,edges):
        self.reversed_edges = {}
        for k,v in edges.items():
            for l in v:
                if l not in self.reversed_edges:
                    self.reversed_edges[l]=[]
                if k not in self.reversed_edges[l]:
                    self.reversed_edges[l].append(k)
    def explore_scc(self, node, component):
        self.explored.add(node)
        self.scc[node] = component
        for neighbor in self.reversed_edges.get(node, []):
            if neighbor not in self.explored:
                self.explore_scc(neighbor, component)
    
    def SCC(self):

        self.reverse(self.edges)
        desending_post = dict(sorted(self.post.items(), key=lambda item: item[1], reverse=True)).keys()
        component = 0
        for node in desending_post:
            if node not in self.explored:
                component+=1
                self.explored.add(node)
                self.explore_scc(node,component)
        return self.scc
if __name__ =='__main__':
    nodes = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']


    a = st.multiselect('Select Node A adjacency:', [node for node in nodes if node != 'A'])
    b = st.multiselect('Select Node B adjacency:', [node for node in nodes if node != 'B'])
    c = st.multiselect('Select Node C adjacency:', [node for node in nodes if node != 'C'])
    d = st.multiselect('Select Node D adjacency:', [node for node in nodes if node != 'D'])
    e = st.multiselect('Select Node E adjacency:', [node for node in nodes if node != 'E'])
    f = st.multiselect('Select Node F adjacency:', [node for node in nodes if node != 'F'])
    g = st.multiselect('Select Node G adjacency:', [node for node in nodes if node != 'G'])
    h = st.multiselect('Select Node H adjacency:', [node for node in nodes if node != 'H'])
    i = st.multiselect('Select Node I adjacency:', [node for node in nodes if node != 'I'])
    j = st.multiselect('Select Node J adjacency:', [node for node in nodes if node != 'J'])
    k = st.multiselect('Select Node K adjacency:', [node for node in nodes if node != 'K'])
    l = st.multiselect('Select Node L adjacency:', [node for node in nodes if node != 'L'])
    m = st.multiselect('Select Node M adjacency:', [node for node in nodes if node != 'M'])
    n = st.multiselect('Select Node N adjacency:', [node for node in nodes if node != 'N'])

    output_dic = {}

    for idx,i in enumerate([a,b,c,d,e,f,g,h,i,j,k,l,m,n]):
        if i:
            output_dic[nodes[idx]]=i

    st.write(f"Edges: {output_dic}")
    st.code(output_dic,language='python')
    
    generate_scc = st.button('calculate SCC')
    if generate_scc:
        nodes = []
        for l in output_dic.values():
            nodes.extend(l)
        nodes = sorted(set(nodes + list(output_dic.keys())))
        st.write(f' nodes are {nodes}')
        gh = DFS(nodes,output_dic)
        pre,post = gh.run_DFS()
        st.write(f'Pre order numbers are {pre} and post are {post}')
        st.write(f' SCC group is {gh.SCC()}')


