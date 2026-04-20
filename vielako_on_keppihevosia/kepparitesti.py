
from keppihevonen import Keppihevonen
from kepparitalli import Kepparitalli



def testaa_hevosia():
    k1 = Keppihevonen("Jaska", 0.75, True)
    k2 = Keppihevonen("Tumppi", 0.9, False)

    k1_ulkonäkö = k1.merkkijonomuodossa()
    print(k1_ulkonäkö)

    k2_un = k2.merkkijonomuodossa()
    print(k2_un)

    k1.kasva_sentti()
    print(k1.merkkijonomuodossa())
    print(k2.merkkijonomuodossa())
  
    #k1.__pituus = 1.15
    #print(k1.__pituus)
    print()
    print(k1.merkkijonomuodossa())
    print(k2.merkkijonomuodossa())

    print("here: ")
    print(k1)


def testaa_tallia():
    print("Tallitesti alkaa: ")
    k1 = Keppihevonen("Jaska", 0.75, True)
    k2 = Keppihevonen("Tumppi", 0.9, False)
    k3 = Keppihevonen("Ansku", 0.67, False)
    k4 = Keppihevonen("Jansku", 0.67, False)


    t1 = Kepparitalli("Turku A-ryhmä", 46)
    t1.lisää(k1)
    t1.lisää(k2)
    t1.lisää(k3)
    t1.lisää(k4)
    t1.lisää(k1)
    t1.elämöi()




testaa_hevosia()


testaa_tallia()


