from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import *
from DatabaseFinal.DBManager import *


columns = ['Nome', 'Scuola', 'Livello', 'Classe']

class FrameSpells(QFrame):
    def __init__(self, db, parent=None):
        super(FrameSpells, self).__init__(parent)
        self.parent = parent
        self.resize(857, 464)
        self.db = db
        self.spells = self.db.getSpells()
        self.vbox = QVBoxLayout()
        self.tableSpells = Table_Spells(self.spells, len(self.spells), len(columns))

        #layout button Cancella/Inserisci
        self.hboxSouth = QHBoxLayout()
        self.buttonDelete = QPushButton("Elimina Incantesimo")
        self.buttonDelete.clicked.connect(self.eventButtonDelete)
        self.buttonNewSpell = QPushButton("Aggiungi Incantesimo")
        #self.buttonNewSpell.clicked.connect(self.eventButtonNewSpell)
        self.hboxSouth.addWidget(self.buttonDelete)
        self.hboxSouth.addWidget(self.buttonNewSpell)

        self.vbox.addWidget(self.tableSpells)
        self.vbox.addLayout(self.hboxSouth)
        self.setLayout(self.vbox)

    def eventButtonDelete(self):
        try:
            spellID = self.tableSpells.selectedItems()[0].text()
            self.db.deleteSpell(spellID)
            self.spells = self.db.getSpells()
            self.tableSpells.removeRow(self.tableSpells.currentRow())
            #self.tableSpells.updateTable(self.spells)
        except(IndexError):
            msg = QMessageBox()
            msg.setWindowTitle("Frame Spell")
            msg.setText("Selezionare un incantesimo prima di eliminarlo")
            msg.exec_()

    '''
    def eventButtonNewSpell(self):
        if(isinstance(self.parent, QMainWindow)):
            self.parent.setCentralWidget(self.frameNewSpell)
    '''




class Table_Spells(QTableWidget):
    def __init__(self, spells, *args):
        QTableWidget.__init__(self, *args)
        self.columns = columns
        self.spells = spells
        self.setData()
        # Font
        self.setFont(QFont('Rockwell', 20))
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)


    def setData(self):
        for m, item in enumerate(self.spells):
            nome = QTableWidgetItem(item.nome)
            nome.setFont(QFont('Rockwell Condensed', 15))
            scuola = QTableWidgetItem(item.scuola)
            scuola.setFont(QFont('Rockwell Condensed', 15))
            livello = QTableWidgetItem(item.livello)
            livello.setFont(QFont('Rockwell Condensed', 15))
            classe = QTableWidgetItem(item.classe)
            classe.setFont(QFont('Rockwell Condensed', 15))
            self.setItem(m, 0, nome)
            self.setItem(m, 1, scuola)
            self.setItem(m, 2, livello)
            self.setItem(m, 3, classe)
        self.setHorizontalHeaderLabels(self.columns)


def main(args):
    app = QApplication(args)
    db = DB_Manager('test.db')
    window = QMainWindow()
    frame = FrameSpells(db, window)
    window.setCentralWidget(frame)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)