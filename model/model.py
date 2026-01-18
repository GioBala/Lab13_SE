import copy

import networkx as nx
from database.dao import DAO

class Model:

    def __init__(self):
        self.G = nx.DiGraph()
        self.cammino_migliore=[]
        self.peso_max=0


    def crea_grafo(self):
        self.G = nx.DiGraph()
        nodi=DAO.get_nodi()
        self.G.add_nodes_from(nodi)
        corr=DAO.get_archi()
        a=set()
        for i in corr:
            a.add(i)
        #print(self.G)
        archi={}
        for i in a:
            if (i[0],i[1]) not in archi.keys():
                archi[i[0],i[1]]=i[4]
            else:
                archi[i[0],i[1]]=archi[i[0],i[1]]+i[4]
        for k,i in archi.items():
            self.G.add_edge(k[0],k[1],weight=i)
        return len(self.G.nodes),len(self.G.edges)


    def get_min_max(self):
        min=float('inf')
        max=-float('inf')
        for u,v in self.G.edges():
            p=self.G.get_edge_data(u,v,'weight')
            peso=p['weight']
            if peso<min:
                min=peso
            if peso>max:
                max=peso
        return min,max

    def get_soglia(self,soglia):
        mi=0
        ma=0
        for u,v in self.G.edges():
            p=self.G.get_edge_data(u,v,'weight')
            peso=p['weight']
            if peso<soglia:
                mi+=1
            if peso>soglia:
                ma+=1
        return mi,ma


    def get_cammino(self,soglia):
        self.cammino_migliore=[]
        self.peso_max=0
        for i in list(self.G.nodes()):
            self.ricorsione(i,[],0,soglia)
        s=f"Numero di archi percorso più lungo: {len(self.cammino_migliore)}\n"
        s=s+f"Peso cammino massimo: {self.peso_max}\n"
        for i in self.cammino_migliore:
            s=s+f"{i[0]} --> {i[1]}: {i[2]}\n"
        return s

    def ricorsione(self,nodo,percorso,peso,soglia):
        #percorso.append(soglia)
        #print(percorso)
        n=list(self.G.successors(nodo))
        if peso>self.peso_max:
            self.peso_max=peso
            self.cammino_migliore=copy.deepcopy(percorso)
        for i in n:
            p = self.G.get_edge_data(nodo, i, 'weight')
            pe = p['weight']
            if (nodo,i,pe) not in percorso and pe>soglia:
                percorso.append((nodo,i,pe))
                self.ricorsione(i,percorso,peso+pe,soglia)
                percorso.pop()



