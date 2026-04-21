from keppihevonen import Keppihevonen
from kepparitalli import Kepparitalli

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

def test4():
    print("Task 4...")
    k1 = Keppihevonen("Ronaldo", 0.75, True)
    k2 = Keppihevonen("Messi", 0.9, False)
    k3 = Keppihevonen("Mbappe", 0.67, True)
    k4 = Keppihevonen("Buffon", 0.67, False)

    t1 = Kepparitalli("Turku F-ryhmä", 33)
    t1.lisää(k1)
    t1.lisää(k2)
    t1.lisää(k3)
    t1.lisää(k4)
    t1.lisää(k1)

    f = "task4.txt"
    t1.tallenna_tiedostoon(f)


# test2()

# test3()

test4()