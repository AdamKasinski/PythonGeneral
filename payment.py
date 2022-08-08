from datetime import datetime
from paymentTerminal import PaymentTerminal


class Payment():

    def __init__(self,client, paymentTerminal):
        self.client = client
        self.time = datetime.now()
        self.paymentTerminal = paymentTerminal
    
    def addLiability(self):
        self.paymentTerminal.addTransaction(self.time,self.client)
    