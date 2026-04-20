
class Kepparitalli:

    def __init__(self, tallin_nimi, kepparimaksimi):
        """Alustaa uuden tallin tyhjäksi ja lailliseen tilaan."""
        self.__nimi = tallin_nimi
        self.__paikkojen_max_lkm = kepparimaksimi
        self.__kepparit = []

 
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

            


 