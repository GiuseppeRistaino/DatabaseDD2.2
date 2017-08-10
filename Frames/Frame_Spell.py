# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrameSpell.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Frame_Spell(QFrame):
    def __init__(self, parent=None):
        super(Frame_Spell, self).__init__(parent)
        self.setObjectName("Form_Spell")
        self.resize(868, 666)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel()
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.labelNome = QLabel()
        self.labelNome.setObjectName("labelNome")
        self.verticalLayout.addWidget(self.labelNome)
        self.labelScuola = QLabel()
        self.labelScuola.setObjectName("labelScuola")
        self.verticalLayout.addWidget(self.labelScuola)
        self.labelLivello = QLabel()
        self.labelLivello.setObjectName("labelLivello")
        self.verticalLayout.addWidget(self.labelLivello)
        self.labelClasse = QLabel()
        self.labelClasse.setObjectName("labelClasse")
        self.verticalLayout.addWidget(self.labelClasse)
        self.labelRaggioAzione = QLabel()
        self.labelRaggioAzione.setObjectName("labelRaggioAzione")
        self.verticalLayout.addWidget(self.labelRaggioAzione)
        self.labelRestInc = QLabel()
        self.labelRestInc.setObjectName("labelRestInc")
        self.verticalLayout.addWidget(self.labelRestInc)
        self.labelTiroSalvezza = QLabel()
        self.labelTiroSalvezza.setObjectName("labelTiroSalvezza")
        self.verticalLayout.addWidget(self.labelTiroSalvezza)
        self.labelTempoLancio = QLabel()
        self.labelTempoLancio.setObjectName("labelTempoLancio")
        self.verticalLayout.addWidget(self.labelTempoLancio)
        self.labelDurata = QLabel()
        self.labelDurata.setObjectName("labelDurata")
        self.verticalLayout.addWidget(self.labelDurata)
        self.labelBersaglio = QLabel()
        self.labelBersaglio.setObjectName("labelBersaglio")
        self.verticalLayout.addWidget(self.labelBersaglio)
        self.labelComponenti = QLabel()
        self.labelComponenti.setObjectName("labelComponenti")
        self.verticalLayout.addWidget(self.labelComponenti)
        self.labelDescrizione = QLabel()
        self.labelDescrizione.setObjectName("labelDescrizione")
        self.verticalLayout.addWidget(self.labelDescrizione)

        self.retranslateUi()

    def retranslateUi(self, ):
        self.setWindowTitle("Frame Spell")
        self.label.setText("<html><head/><body><p><br/><span style=\" font-size:15pt; font-weight:600;\">Incantesimo</span></p></body></html>")
        self.labelNome.setText("Nome: ")
        self.labelScuola.setText("Scuola: ")
        self.labelLivello.setText("Livello: ")
        self.labelClasse.setText("Classe: ")
        self.labelRaggioAzione.setText("Raggio di azione: ")
        self.labelRestInc.setText("Resistenza agli incantesimi: ")
        self.labelTiroSalvezza.setText("Tiro Salvezza: ")
        self.labelTempoLancio.setText("Tempo di lancio: ")
        self.labelDurata.setText("Durata: ")
        self.labelBersaglio.setText("Bersaglio: ")
        self.labelComponenti.setText("Componenti: ")
        self.labelDescrizione.setText("Descrizione: ")

