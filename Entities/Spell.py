
ATTRIBUTE_SPELL = ["Nome", "Scuola", "Livello", "Classe", "Raggio di azione", "Resistenza agli incantesimi", "Tiro salvezza", "Tempo di lancio", "Descrizione", "Durata",
                       "Bersaglio", "Componenti"]

class Spell():

    def __init__(self, nome, scuola, livello, classe, raggio_di_azione, res_inc, tiro_salvezza, tempo_di_lancio,
                 descrizione, durata, bersaglio, componenti):
        self.nome = nome
        self.scuola = scuola
        self.livello = livello
        self.classe = classe
        self.raggio_di_azione = raggio_di_azione
        self.res_inc = res_inc
        self.tiro_salvezza = tiro_salvezza
        self.tempo_di_lancio = tempo_di_lancio
        self.descrizione = descrizione
        self.durata = durata
        self.bersaglio = bersaglio
        self.componenti = componenti