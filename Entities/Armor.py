
class Armor():
    #Velocity 9 = velocità per chi ha 9 metri di velocità
    #Velocity 6 = velocità per chi ha 6 metri di velocità
    def __init__(self, nome, costo, bonus_arm_scud, bonus_des_max, penality, fallimento_inc, velocity_9, velocity_6,
                 peso, descrizione, speciale, durability, img):
        self.nome = nome
        self.descrizione = descrizione
        self.costo = costo
        self.bonus_arm_scud = bonus_arm_scud
        self.bonus_des_max = bonus_des_max
        self.penality = penality
        self.fallimento_inc = fallimento_inc
        self.velocity_9 = velocity_9
        self.velocity_6 = velocity_6
        self.speciale = speciale
        self.img = img
        self.durability = durability
        self.peso = peso