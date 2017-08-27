
class Weapon():

    def __init__(self, nome, tipo, costo, danni_p, danni_m, critico, gittata, peso, speciale, descrizione, durability,  img):
        self.nome = nome
        self.descrizione = descrizione
        self.tipo = tipo
        self.costo = costo
        self.danni_p = danni_p
        self.danni_m = danni_m
        self.critico = critico
        self.gittata = gittata
        self.peso = peso
        self.speciale = speciale
        self.durability = durability
        self.img = img