
from keppihevonen import Keppihevonen
from kepparitalli import Kepparitalli



def testaa_hevosia():
    k1 = Keppihevonen("Alex", 0.75, True)
    k2 = Keppihevonen("Vladimir", 0.9, False)

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
    k1 = Keppihevonen("Horse1", 0.75, True)
    k2 = Keppihevonen("Horse2", 0.9, False)
    k3 = Keppihevonen("Horse3", 0.67, False)
    k4 = Keppihevonen("Horse4", 0.67, False)


    t1 = Kepparitalli("Turku A-ryhmä", 46)
    t1.lisää(k1)
    t1.lisää(k2)
    t1.lisää(k3)
    t1.lisää(k4)
    t1.lisää(k1)
    t1.elämöi()

def test2():
    print("Task 2...")
    horse = Keppihevonen("Viktor", 0.9, True)
    tiedosto = open("task2.txt", "w")
    horse.tallenna_tiedostoon(tiedosto)
    tiedosto.close()

def test3():
    print("Task 3...")
    tiedosto = open("task3.txt", "r")
    horse = Keppihevonen.lue_tiedostosta(tiedosto)
    print(horse)
    tiedosto.close()


# test2()

test3()

# testaa_hevosia()

# testaa_tallia()


