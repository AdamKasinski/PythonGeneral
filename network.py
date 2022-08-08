import numpy as np
import networkx as nx

class Network:
    def __init__(self):
        self.edges = []
        self.G = nx.Graph()
    
    def addNewFriendship(self,*clients):
        self.G.add_edge(*clients)
        self.G[clients[0]][clients[1]]['weight'] = 1

    def updateFriendship(self,*clients):
        self.G[clients[0]][clients[1]]['weight'] += 1


