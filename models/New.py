from flask import Flask
New = Flask(__name__)


class New:

    def __init__(self, headLine='Feijóo conquista su cuarta mayoría absoluta y Urkullu se refuerza', newsBody='En tiempos de pandemia, estabilidad política. Las primeras elecciones del coronavirus, que llevaron este domingo a las urnas a gallegos y vascos, enviaron un mensaje muy claro. El gallego Alberto Núñez Feijóo confirmó su cuarta mayoría absoluta con otro triunfo arrollador sobre la izquierda, un éxito al que no se puede acercar ni de lejos cualquier otro dirigente territorial del PP. En Euskadi, el lehendakari Iñigo Urkullu llevó al PNV a su mejor resultado desde 1984, con cerca del 40% de los votos. Para los dos partidos en el Gobierno de España, la jornada fue más aciaga, sobre todo para Podemos, que salió zarandeado: quedó fuera del Parlamento gallego y perdió la mitad de su representación en Euskadi. Los socialistas se estancan en las dos comunidades y en Galicia incluso les supera el BNG, el otro gran triunfador de la noche, junto a EH Bildu.'):
        self.headLine = headLine
        self.newsBody = newsBody

    def ReadHeadLine(self):
        return self.headLine

    def readNewsBody(self):
        return self.newsBody



