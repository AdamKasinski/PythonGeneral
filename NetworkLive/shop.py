from payment import Payment
from paymentTerminal import PaymentTerminal
from network import Network
from payment import Payment

class Shop:
    def __init__(self,name):
        self.name = name
        self.terminals = []
        self.network = Network()
        self.clients = []
    
    def addTerminal(self):
        self.terminals.append(PaymentTerminal(len(self.terminals)+1,self.network))
    
    def addPayment(self,client,terminal):
        payment = Payment(client,self.terminals[terminal])
        payment.addLiability()

