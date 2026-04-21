from keppihevonen import Keppihevonen

class Kepparitalli:

    def __init__(self, tallin_nimi, kepparimaksimi):
        """Alustaa uuden tallin tyhjäksi ja lailliseen tilaan."""
        self.__nimi = tallin_nimi
        self.__paikkojen_max_lkm = kepparimaksimi
        self.__kepparit = []
    
    def anna_nimi(self):
        return self.__nimi

    def anna_maksimi(self):
        return self.__paikkojen_max_lkm
 
    def tallissa_tilaa(self):
        """Onko tallissa tilaa?"""
        return len(self.__kepparit) < self.__paikkojen_max_lkm


    def lisää(self, keppari):
        """Lisää kepparin talliin, kun tilaa on.
        Alkuehto: self.tallissa_tilaa() """
       
        assert self.tallissa_tilaa(), "Tallissa ei ole tarpeeksi tilaa." 
        self.__kepparit.append(keppari)


    def elämöi(self):
        """Tulostaa tallin nykyhetken elämöinnin ruudulle."""
        for hepo in self.__kepparit:
            print(hepo)

    def tallenna_tiedostoon(self, tiedoston_nimi):
        tiedosto = open(tiedoston_nimi, "w")
        rivi = self.__nimi + ";" + str(self.__paikkojen_max_lkm) + "\n"
        tiedosto.write(rivi)
        for horse in self.__kepparit:
            horse.tallenna_tiedostoon(tiedosto)
        tiedosto.close()

    @staticmethod
    def lue_tiedostosta(tiedoston_nimi):
        tiedosto = open(tiedoston_nimi, "r")

        rivi = tiedosto.readline()
        rivi = rivi.strip()
        osat = rivi.split(";")

        talli = Kepparitalli(osat[0], int(osat[1]))

        horse = Keppihevonen.lue_tiedostosta(tiedosto)
        while horse is not None:
            talli.lisää(horse)
            horse = Keppihevonen.lue_tiedostosta(tiedosto)

        tiedosto.close()
        return talli 
    
        

            

 