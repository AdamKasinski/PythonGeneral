import unittest
from paymentTerminal import PaymentTerminal
import networkx as nx
from datetime import datetime
import time
from network import Network

class TestpaymentTerminal(unittest.TestCase):

    def test_makeRelation(self):
        '''
        test czy sieć prawidłowo działa
        
        '''
        pt = PaymentTerminal(1, Network())
        pt.addTransaction(datetime.now(), 1)
        pt.addTransaction(datetime.now(), 2)
        pt.addTransaction(datetime.now(), 7)
        time.sleep(2.1)
        pt.addTransaction(datetime.now(), 3)
        pt.addTransaction(datetime.now(), 4)
        time.sleep(2.1)
        pt.addTransaction(datetime.now(), 5)
        pt.addTransaction(datetime.now(), 6)

        sec = nx.Graph()
        sec.add_edge(1,2)
        sec.add_edge(2,7)
        sec.add_edge(1,7)
        sec.add_edge(3,4)
        sec.add_edge(5,6)

        self.assertEqual(pt.network.G.edges,sec.edges)
        
if __name__ == '__main__':
    unittest.main()