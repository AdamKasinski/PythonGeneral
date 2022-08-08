from network import Network
import networkx as nx
from itertools import islice


class PaymentTerminal:

    def __init__(self,terminalID, network):
        self.terminalID = terminalID
        self.transactions = []
        self.network = network


    def addTransaction(self,time,clientID):
        self.transactions.append([time, clientID])
        if len(self.transactions) >= 2:
            self.makeRelation()



    def makeRelation(self):
        invTrans = self.transactions[::-1]
        for transactionValue in (invTrans[1:]):
            res = (invTrans[0][0] - transactionValue[0]).total_seconds()
            if res < 0.05: #wspomniana w pliku main czas, po którym relacja między klientami nie jest powiązana, można to interpretować jako obsługa innego stolika
                if self.network.G.has_edge(invTrans[0][1],transactionValue[1]):
                    self.network.updateFriendship(invTrans[0][1],transactionValue[1])
                else:
                    self.network.addNewFriendship(invTrans[0][1],transactionValue[1])
            else:
                break
        


