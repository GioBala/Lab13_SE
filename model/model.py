import networkx as nx
from database.dao import DAO
from model import interazione
from model.interazione import Interazione


class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.map={}

    def Crea_graph(self):
        archi=self.get_Archi()
        #print(archi)
        self.G.add_weighted_edges_from(archi)
        n_archi=self.G.number_of_edges()
        n_nodi=self.G.number_of_nodes()
        min,max=self.get_min_max()
        return n_nodi, n_archi, min,max

    def get_Archi(self):
        interazioni=DAO.get_interazione()
        geni=DAO.get_gene()
        for gene in geni:
            self.map[gene.id]=gene
        archi=[]
        edges = {}
        for i in interazioni:
            if i.id_gene1 in self.map.keys() and i.id_gene2 in self.map.keys():
                if int(self.map[i.id_gene1].cromosoma)   != int(self.map[i.id_gene2].cromosoma) and int(self.map[i.id_gene1].cromosoma)!=0 and int(self.map[i.id_gene2].cromosoma)!=0 :
                    if (int(self.map[i.id_gene1].cromosoma),int(self.map[i.id_gene2].cromosoma),i.id_gene1,i.id_gene2,i.correlazione) not in archi:
                        archi.append((int(self.map[i.id_gene1].cromosoma),int(self.map[i.id_gene2].cromosoma),i.id_gene1,i.id_gene2,i.correlazione))
                        if (self.map[i.id_gene1].cromosoma,self.map[i.id_gene2].cromosoma) in edges.keys():
                            edges[(self.map[i.id_gene1].cromosoma, self.map[i.id_gene2].cromosoma)] += i.correlazione
                        else:
                            edges[(self.map[i.id_gene1].cromosoma,self.map[i.id_gene2].cromosoma)]=i.correlazione
                        #print(archi)
        a=[]
        for k,v in edges.items():
            a.append((k[0],k[1],float(v)))
        return a


    def get_min_max(self):
        p = self.G.get_edge_data(1, 2, "weight")
        min=p["weight"]
        max=0
        for u,v in self.G.edges():
            p=self.G.get_edge_data(u,v,"weight")
            if max < float(p["weight"]):
                max=float(p["weight"])
            if min > float(p["weight"]):
                min=float(p["weight"])
        return min,max

    def conta_archi(self,soglia):
        sup=0
        inf=0
        for u,v in self.G.edges():
            p=self.G.get_edge_data(u,v,"weight")
            if p["weight"] > soglia:
                sup+=1
            if p["weight"] < inf:
                inf+=1
        return sup,inf

