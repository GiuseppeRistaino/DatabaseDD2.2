import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from DatabaseFinal.DBManager import *

columns = ['Nome', 'Scuola', 'Livello', 'Classe']


class MyTable(QTableWidget):
    def __init__(self, spells, *args):
        QTableWidget.__init__(self, *args)
        self.columns = columns
        self.spells = spells
        #self.setmydata()
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setData(self):
        for m, item in enumerate(self.spells):
            nome = QTableWidgetItem(item.nome)
            scuola = QTableWidgetItem(item.scuola)
            livello = QTableWidgetItem(item.livello)
            classe = QTableWidgetItem(item.classe)
            self.setItem(m, 0, nome)
            self.setItem(m, 1, scuola)
            self.setItem(m, 2, livello)
            self.setItem(m, 3, classe)
        self.setHorizontalHeaderLabels(self.columns)

def main(args):
    app = QApplication(args)
    db = DB_Manager('test.db')
    spells = db.getSpells()
    table = MyTable(spells, len(spells), len(columns))
    table.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)