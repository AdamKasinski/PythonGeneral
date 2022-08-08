from networkx.algorithms.shortest_paths import weighted
from networkx.readwrite import edgelist
from shop import Shop
from payment import Payment
import random
import networkx as nx
import matplotlib.pyplot as plt
import time
from paymentTerminal import PaymentTerminal
import random

'''
klient przestawia symulację restauracji. Do restauracji przychodzą ludzie i siadają przy stoliku. Przy jednym stoliku siadają znajomi i są obsługiwani za pomocą
jednego terminala. Terminal aktualizuje sieć - dodaje połączenie między wierzchołkami - klientami - jeżeli dwie transakcje są zawarte w zbyt długim odcinku czasu,
klienci nie są ze sobą połączeni.
Celem symulacji jest przestawienie sieci w której wierzchołek to klient, połączenie to "znajomość" klientów - im mocniejszy kolor, tym ludzie częściej razem przychodzą.
Sieć może być przydatna do obliczania różnych miar centralności.
W celu "optymalizacji" wyświetla się tylko sieć końcowa, nie obliczam miar centralności - pakiet networkx ma je zaimplementowane, natomiast złożoność jest na tyle duża,
że na wynik trzeba długo czekać
'''

class Main:

    def __init__(self):
        '''
        program main - dla prostoty, tutaj jest tworzona populacja kupujących, tworzone obiekty sklepu, tutaj "dokonują się" transakcje
        
        '''
        self.shop = Shop("restauracja")
        for i in range(3):
            self.shop.addTerminal()
        self.clientsID = self.dodajKlientow(100)
        ludzie = list(self.clientsID.keys());

        for i in range(300):
            ile = random.choice([0,1,2,3,4]) # zakładam że i to obsługa jednego stolika - przy nim może być kilka osób, wszyscy są obsługiwani jednym terminalem
            terminal = random.choice(range(3))
            for j in range(ile):
                a = self.losuj(ludzie)
                self.shop.addPayment(a,terminal)
                a = self.losuj(self.clientsID[a]) #przy jednym stoliku siedzą znajomi
            time.sleep(0.07)


        edges,weights = zip(*nx.get_edge_attributes(self.shop.network.G,'weight').items())
        nx.draw(self.shop.network.G, with_labels = True,pos = nx.spring_layout(self.shop.network.G),edgelist=edges, edge_color=weights,edge_cmap=plt.cm.Blues)
        plt.show()


    def losuj(self,lista):
        if len(lista) != 0:
            return random.choice(lista)


    def losujZnajomych(self,klient,iluKlientowOgolem):
        sample = random.sample(range(iluKlientowOgolem),k=random.randint(0,4))
        if klient in sample:
            sample.pop(sample.index(klient))
        return list(set(sample))


    def dodajKlientow(self,number): #wolałem użyć podwójnego fora niż rozwiązać problem rekurencyjnie, ponieważ wydaje mi się to bardziej czytelne i efektywniejsze
        '''
        klienci są trzymani jako klucze słownika, wartości to lista ich znajomych, jeżeli klient 1 jest znajomym klienta 0, to automatycznie klient 0 jest znajomym
        klienta 1
        '''
        
        clients = {}
        for klient in range(number):
            if klient not in clients:
                clients[klient] = self.losujZnajomych(klient,number)
                for znajomy in clients[klient]:
                    if znajomy not in clients:
                        clients[znajomy] = [klient]
                    else:
                        if klient not in clients[znajomy]:
                            clients[znajomy].append(klient)

            else:
                znajomi = self.losujZnajomych(klient,number)
                clients[klient] = list(set([*clients[klient],*znajomi]))
                for znajomy in clients[klient]:
                    if znajomy not in clients:
                        clients[znajomy] = [klient]
                    else:
                        if klient not in clients[znajomy]:
                            clients[znajomy].append(klient)
            
        return clients



Main()