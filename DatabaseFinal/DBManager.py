import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui, QtSql

from Entities.Spell import *


class DB_Manager():

    TABLE_ABILITY = "Ability"
    ATTRIBUTE_ABILITY = ["Nome", "Descrizione", "Prova", "Azione", "Ritentare", "Speciale",
                         "Sinergia", "Restrizioni", "Senza_addestramento"]
    TABLE_WEAPON = "Arma"
    ATTRIBUTE_WEAPON = ["Nome", "Tipo", "Integrità", "Costo", "Danni_piccola", "Danni_media",
                        "Critico", "Gittata", "Peso"]
    TABLE_SPELL = "Spell"
    ATTRIBUTE_SPELL = ["Nome", "Scuola", "Livello", "Classe", "Raggio di azione", "Resistenza agli incantesimi",
                       "Tiro salvezza", "Tempo di lancio", "Descrizione", "Durata", "Bersaglio", "Componenti"]
    TABLE_INGREDEINT = "Ingrediente"
    ATTRIBUTE_INGREDIENT = ["Nome", "Luogo", "Percentuale", "Descrizione", "Costo"]
    TABLE_MONSTER = "Mostro"
    ATTRIBUTE_MONSTER = ["Nome", "Tipo", "Allineamento" "Taglia", "GS", "PE", "Iniziativa", "Sensi", "CA", "PF",
                         "Tempra", "Riflessi", "Volontà", "Resistenze", "Velocità", "Attacco_mischia",
                         "Attacco_distanza",
                         "Attacchi_speciali", "Incantesimi", "Portata", "Linguaggi",
                         "Forza", "Destrezza", "Costituzione", "Intelligenza", "Saggezza", "Carisma",
                         "AB", "BMC", "DMC", "Talenti", "Abilità", "QS", "Ambiente", "Tesoro", "CS", "Descrizione",
                         "Immagine", "Tabelle", "Icona"]
    TABLE_ITEM = "Oggetti"
    ATTRIBUTE_ITEM = ["Nome", "Resistenza", "Valore", "Peso", "Descrizione", "Immagine"]
    TABLE_POTION = "Pozione"
    ATTRIBUTE_POTION = ["Nome", "Ricetta", "Tempo", "Effetto", "CD", "Valore"]
    TABLE_TALENT = "Talenti"
    ATTRIBUTE_TALENT = ["Nome", "Descrizione", "Prerequisito", "Beneficio", "Normale", "Speciale"]


    def __init__(self, DB_Name):
        self.createDB(DB_Name)

    #Crea il database
    def createDB(self, DB_Name):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(DB_Name)
        if not db.open():
            QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                       QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                     "This example needs SQLite support. Please read "
                                                     "the Qt SQL driver documentation for information "
                                                     "how to build it.\n\n"
                                                     "Click Cancel to exit."),
                                       QtGui.QMessageBox.Cancel)
            return False
        query = QtSql.QSqlQuery()
        query.exec_("create table Mostro (Nome Text primary key, "
                    "Tipo Text, Allineamento Text, Taglia Text, GS Text, PE Text, Iniziativa Text, Sensi Text, CA Text,"
                    "PF Text, Tempra Text, Riflessi Text, Volontà Text, Resistenze Text, Velocità Text, Attacco_mischia Text, Attacco_distanza Text,"
                    "Attacchi_speciali Text, Incantesimi Text, Portata Text, Linguaggi Text, Forza Text, Destrezza Text, Costituzione Text,"
                    "Intelligenza Text, Saggezza Text, Carisma Text, AB Text, BMC Text, DMC Text, Talenti Text, Abilità Text,"
                    "QS Text, Ambiente Text, Tesoro Text, CS Text, Descrizione Text, Immagine BLOB, Tabelle BLOB, Icona BLOB)")

        query.exec_("create table Spell (Nome Text primary key, "
                    "Scuola Text, Livello Text, Classe Text, Raggio_di_azione Text, Resistenza_agli_incantesimi Text, "
                "Tiro_salvezza Text, Tempo_di_lancio Text, Descrizione Text, Durata Text, Bersaglio Text, Componenti Text)")
        return True


    #Inserisce un Mostro nel Database
    def insertMonster(self, Nome, Tipo, Allineamento, Taglia, GS, PE, Iniziativa, Sensi, CA, PF,
                      Tempra, Riflessi, Volontà, Resistenze, Velocità, Attacco_mischia, Attacco_distanza,
                      Attacchi_speciali, Incantesimi, Portata, Linguaggi,
                      Forza, Destrezza, Costituzione, Intelligenza, Saggezza, Carisma,
                      AB, BMC, DMC, Talenti, Abilità, QS, Ambiente, Tesoro, CS, Descrizione,
                      Path_Immagine, Path_Tabelle, Path_Icona):
        query = QtSql.QSqlQuery()
        query.prepare(
            "insert into Mostro (Nome, Tipo,Allineamento,Taglia,GS, PE,Iniziativa,Sensi,CA, "
            "PF,Tempra,Riflessi,Volontà, Resistenze,Velocità,Attacco_mischia,Attacco_distanza, "
            "Attacchi_speciali,Incantesimi,Portata,Linguaggi, "
            "Forza,Destrezza,Costituzione,Intelligenza, Saggezza,Carisma,AB,BMC, DMC,Talenti,Abilità,QS, "
            "Ambiente,Tesoro,CS,Descrizione,Immagine,Tabelle,Icona) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
            "?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"
            "?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"
            "?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")

        # Immagine
        pixmapImg = QPixmap(Path_Immagine)
        bytesImg = QByteArray()
        bufferImg = QBuffer(bytesImg)
        bufferImg.open(QIODevice.WriteOnly)
        pixmapImg.save(bufferImg, "jpg")

        # Tabelle
        pixmapTab = QPixmap(Path_Tabelle)
        bytesTab = QByteArray()
        bufferTab = QBuffer(bytesTab)
        bufferTab.open(QIODevice.WriteOnly)
        pixmapTab.save(bufferTab, "jpg")

        # Icona
        pixmapIcon = QPixmap(Path_Icona)
        bytesIcon = QByteArray()
        bufferIcon = QBuffer(bytesIcon)
        bufferIcon.open(QIODevice.WriteOnly)
        pixmapIcon.save(bufferIcon, "jpg")

        query.bindValue(0, Nome)
        query.bindValue(1, Tipo)
        query.bindValue(2, Allineamento)
        query.bindValue(3, Taglia)
        query.bindValue(4, GS)
        query.bindValue(5, PE)
        query.bindValue(6, Iniziativa)
        query.bindValue(7, Sensi)
        query.bindValue(8, CA)
        query.bindValue(9, PF)
        query.bindValue(10, Tempra)
        query.bindValue(11, Riflessi)
        query.bindValue(12, Volontà)
        query.bindValue(13, Resistenze)
        query.bindValue(14, Velocità)
        query.bindValue(15, Attacco_mischia)
        query.bindValue(16, Attacco_distanza)
        query.bindValue(17, Attacchi_speciali)
        query.bindValue(18, Incantesimi)
        query.bindValue(19, Portata)
        query.bindValue(20, Linguaggi)
        query.bindValue(21, Forza)
        query.bindValue(22, Destrezza)
        query.bindValue(23, Costituzione)
        query.bindValue(24, Intelligenza)
        query.bindValue(25, Saggezza)
        query.bindValue(26, Carisma)
        query.bindValue(27, AB)
        query.bindValue(28, BMC)
        query.bindValue(29, DMC)
        query.bindValue(30, Talenti)
        query.bindValue(31, Abilità)
        query.bindValue(32, QS)
        query.bindValue(33, Ambiente)
        query.bindValue(34, Tesoro)
        query.bindValue(35, CS)
        query.bindValue(36, Descrizione)
        query.bindValue(37, bytesImg)
        query.bindValue(38, bytesTab)
        query.bindValue(39, bytesIcon)
        query.exec_()

    # Inserisce un Incantesimo nel Database
    # APPROVED BY VREXAS
    def insertSpell(self, spell):
        query = QtSql.QSqlQuery()
        query.prepare(
            "insert into Spell (Nome, Scuola, Livello, Classe, Raggio_di_azione, Resistenza_agli_incantesimi, "
            "Tiro_salvezza, Tempo_di_lancio, Descrizione, Durata, Bersaglio, Componenti) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
            "?, ?)")
        query.bindValue(0, spell.nome)
        query.bindValue(1, spell.scuola)
        query.bindValue(2, spell.livello)
        query.bindValue(3, spell.classe)
        query.bindValue(4, spell.raggio_di_azione)
        query.bindValue(5, spell.res_inc)
        query.bindValue(6, spell.tiro_salvezza)
        query.bindValue(7, spell.tempo_di_lancio)
        query.bindValue(8, spell.descrizione)
        query.bindValue(9, spell.durata)
        query.bindValue(10, spell.bersaglio)
        query.bindValue(11, spell.componenti)
        result = query.exec_()
        return result

    #Restituisce la lista dei nomi delle abilità
    def getListAbility(self):
        queryString = "SELECT * FROM " +self.TABLE_ABILITY
        return self.getListOfOneElementForRow(queryString)

    #Restituisce il dizionario contenente i valori della abilità data
    def getAbility(self, nameAbility):
        queryString = "SELECT * FROM " +self.TABLE_ABILITY +" WHERE " +self.ATTRIBUTE_ABILITY[0] +" = " +"\"" +nameAbility +"\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_ABILITY)

    # Restituisce la lista dei nomi delle armi
    def getListWeapon(self):
        queryString = "SELECT * FROM " + self.TABLE_WEAPON +" ORDER BY " +self.ATTRIBUTE_WEAPON[0]
        return self.getListOfOneElementForRow(queryString)

    #Restituisce il dizionario contenente i valori dell'arma data
    def getWeapon(self, nameWeapon):
        queryString = "SELECT * FROM " +self.TABLE_WEAPON +" WHERE " +self.ATTRIBUTE_WEAPON[0] +" = " +"\"" +nameWeapon +"\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_WEAPON)


    # Restituisce la lista delle spell
    #APPROVED BY VREXAS
    def getSpells(self):
        queryString = "SELECT * FROM " + self.TABLE_SPELL + " ORDER BY " + self.ATTRIBUTE_SPELL[0]
        query = QtSql.QSqlQuery()
        query.exec(queryString)
        result = []
        while (query.next()):
            spell = Spell(query.value(0), query.value(1), query.value(2), query.value(3), query.value(4), query.value(5), query.value(6)
                          , query.value(7), query.value(8), query.value(9), query.value(10), query.value(11))
            result.append(spell)
        return result

    def deleteSpell(self, nome):
        queryString = "DELETE FROM " +self.TABLE_SPELL +" WHERE " +self.ATTRIBUTE_SPELL[0] +" IS '" +nome+"'"
        query = QtSql.QSqlQuery()
        result = query.exec(queryString)
        return result

    # Restituisce il dizionario contenente i valori dalla magia data
    def getMagic(self, nameMagic):
        queryString = "SELECT * FROM " + self.TABLE_MAGIC + " WHERE " + self.ATTRIBUTE_MAGIC[0] + " = " + "\"" + nameMagic + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_MAGIC)

    # Restituisce la lista degli ingredienti
    def getListIngredient(self):
        queryString = "SELECT * FROM " + self.TABLE_INGREDEINT + " ORDER BY " + self.ATTRIBUTE_INGREDIENT[0]
        return self.getListOfOneElementForRow(queryString)


    # Restituisce il dizionario contenente i valori dall'ingrediente dato
    def getIngredient(self, name):
        queryString = "SELECT * FROM " + self.TABLE_INGREDEINT + " WHERE " + self.ATTRIBUTE_INGREDIENT[0] + " = " + "\"" + name + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_INGREDIENT)

    # Restituisce la lista dei mostri
    def getListMonster(self):
        queryString = "SELECT * FROM " + self.TABLE_MONSTER + " ORDER BY " + self.ATTRIBUTE_MONSTER[0]
        return self.getListOfOneElementForRow(queryString)

    # Restituisce il dizionario contenente i valori dal mostro dato
    def getMonster(self, name):
        queryString = "SELECT * FROM " + self.TABLE_MONSTER + " WHERE " + self.ATTRIBUTE_MONSTER[0] + " = " + "\"" + name + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_MONSTER)

    # Restituisce la lista degli oggetti
    def getListItem(self):
        queryString = "SELECT * FROM " + self.TABLE_ITEM + " ORDER BY " + self.ATTRIBUTE_ITEM[0]
        return self.getListOfOneElementForRow(queryString)

    # Restituisce il dizionario contenente i valori dall'oggetto dato
    def getItem(self, name):
        queryString = "SELECT * FROM " + self.TABLE_ITEM + " WHERE " + self.ATTRIBUTE_ITEM[0] + " = " + "\"" + name + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_ITEM)

    # Restituisce la lista delle pozioni
    def getListPotion(self):
        queryString = "SELECT * FROM " + self.TABLE_POTION + " ORDER BY " + self.ATTRIBUTE_POTION[0]
        return self.getListOfOneElementForRow(queryString)


    # Restituisce il dizionario contenente i valori dalla pozione data
    def getPotion(self, name):
        queryString = "SELECT * FROM " + self.TABLE_POTION + " WHERE " + self.ATTRIBUTE_POTION[0] + " = " + "\"" + name + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_POTION)

    # Restituisce la lista degli oggetti
    def getListTalent(self):
        queryString = "SELECT * FROM " + self.TABLE_TALENT + " ORDER BY " + self.ATTRIBUTE_TALENT[0]
        return self.getListOfOneElementForRow(queryString)

    # Restituisce il dizionario contenente i valori dal talento dato
    def getTalent(self, name):
        queryString = "SELECT * FROM " + self.TABLE_TALENT + " WHERE " + self.ATTRIBUTE_TALENT[0] + " = " + "\"" + name + "\""
        return self.getElementsInRowFromKey(queryString, self.ATTRIBUTE_TALENT)

    #restituisce gli elementi per ogni attributo di una data riga
    def getElementsInRowFromKey(self, queryString, attributeList):
        query = QtSql.QSqlQuery()
        query.exec(queryString)
        listItem = []
        while (query.next()):
            for elem in range(0, len(attributeList)):
                listItem.append(query.value(elem))
        return listItem

    def getListOfOneElementForRow(self, queryString):
        query = QtSql.QSqlQuery()
        query.exec(queryString)
        result = []
        while (query.next()):
            result.append(query.value(0))
        return result







if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    db = DB_Manager("test.db")

    file = "hack_00.jpg"
    db.insertMonster('Nome', 'Tipo', 'Allineamento', 'Taglia', 'GS', 'PE', 'Iniziativa', 'Sensi', 'CA',
                  'PF', 'Tempra', 'Riflessi', 'Volontà', 'Resistenze', 'Velocità', 'Attacco_mischia',
                  'Attacco_distanza',
                  'Attacchi_speciali', 'Incantesimi', 'Portata', 'Linguaggi',
                  'Forza', 'Destrezza', 'Costituzione', 'Intelligenza', 'Saggezza', 'Carisma', 'AB', 'BMC', 'DMC',
                  'Talenti', 'Abilità', 'QS',
                  'Ambiente', 'Tesoro', 'CS', 'Descrizione', file, file, file)
    spell = Spell("Nome", "Scuola", "Livello", "Classe", "Raggio di azione", "Resistenza agli incantesimi",
                  "Tiro salvezza", "Tempo di lancio", "Descrizione", "Durata",
                  "Bersaglio", "Componenti")
    db.insertSpell(spell)