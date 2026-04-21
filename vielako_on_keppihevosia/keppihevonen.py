
class Keppihevonen:


    def __init__(self, uusi_nimi, uusi_pituus, onKovapäinen):
        """Alustaa uuden keppihevosen, jonka nimeksi tulee uusi_nimi,
           pituudeksi uusi_pituus (metreinä) ja pään kovuus määräytyy 
           onKovapäinen-bool argumentin mukaan."""
        self.__nimi = uusi_nimi
        self.__pituus = uusi_pituus
        self.__onKova = onKovapäinen

 
    def __str__(self):
        """Palauttaa olion esityksen merkkijonomuodossa."""
        return self.merkkijonomuodossa()


    def merkkijonomuodossa(self):
        """Palauttaa olion esityksen merkkijonomuodossa."""
        palautettava = ""
        palautettava += self.__nimi
        palautettava += ": "
        palautettava += str(self.__pituus)

        if (self.__onKova):
            pää = "[]____ "
        else:
            pää = "()____ "

        palautettava = pää + palautettava
        return palautettava


    def kasva_sentti(self):
        """Kasvattaa keppihevosen kokoa yhden senttimetrin."""
        self.__pituus = self.__pituus + 0.01
    
    def tallenna_tiedostoon(self, avattu_tied):
        assert not avattu_tied.closed
        assert avattu_tied.writable()

        rivi = self.__nimi + ";" + str(self.__pituus) + ";" + str(self.__onKova) + "\n"
        avattu_tied.write(rivi)

    @staticmethod
    def lue_tiedostosta(avattu_tied):
        assert not avattu_tied.closed
        assert avattu_tied.readable()

        rivi = avattu_tied.readline()
        if rivi == "":
            return None
        rivi = rivi.strip()
        osat = rivi.split(";")

        pituus = float(osat[1])
        onKova = (osat[2] == "True")
        newHorse = Keppihevonen(osat[0], pituus, onKova)

        return newHorse
    


