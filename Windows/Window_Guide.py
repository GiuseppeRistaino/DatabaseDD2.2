from PyQt4.QtGui import *
from DatabaseFinal.DBManager import *
from Frames.Frame_Spells import *
from Frames.Frame_New_Spell import *



class Guide_Window(QMainWindow):
    def __init__(self):
        super(Guide_Window, self).__init__()
        self.db = DB_Manager('test.db')
        self.resize(857, 464)

        menu = self.menuBar()

        self.showFrameSpells()

    def showFrameSpells(self):
        frame = FrameSpells(self.db, self)
        frame.buttonNewSpell.clicked.connect(self.showFrameNewSpell)
        self.setCentralWidget(frame)

    def showFrameNewSpell(self):
        frame = Frame_New_Spell(self.db, self)
        frame.buttonOk.clicked.connect(self.showFrameSpells)
        frame.buttonCancel.clicked.connect(self.showFrameSpells)
        self.setCentralWidget(frame)




def main(args):
    app = QApplication(args)
    window = Guide_Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)