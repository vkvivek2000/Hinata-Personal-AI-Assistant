from Hinata import Ui_HinataGui
from PyQt5.QtWidgets import QWidget
from Hinata import Ui_HinataGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, Qt , QTime , QTimer , QDate
from PyQt5.uic import loadUiType
import Main
import sys

class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        Main.Task_Gui()
startExe = MainThread()

class Gui_start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui = Ui_HinataGui()
        self.gui.setupUi(self)
        self.gui.Start.clicked.connect(self.startTask)
        self.gui.Quit.clicked.connect(self.close)

    def updateMovieDynamically(self, state):
        if state == "speaking":
            self.gui.CandySpeakingLabel.raise_()
            self.gui.listeningLabel.hide()
            self.gui.loadingLabel.hide()
        elif state == "listening":
            self.gui.listeningLabel.raise_()
            self.gui.CandySpeakingLabel.hide()
            self.gui.loadingLabel.hide()
        elif state == "loading":
            self.gui.loadingLabel.raise_()
            self.gui.CandySpeakingLabel.hide()
            self.gui.listeningLabel.raise_()

    def startTask(self):

        self.gui.label1 = QtGui.QMovie("C:/Users/vkviv/OneDrive/Desktop/Gui/dec7zp0-b1f90b09-8dd0-4877-9be1-cf990bad3309 (1).gif")
        self.gui.suitdiagnostics.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("C:/Users/vkviv/OneDrive/Desktop/Gui/G.U.I Material/B.G/Iron_Template_1.gif")
        self.gui.ironman.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("C:/Users/vkviv/OneDrive/Desktop/Gui/G.U.I Material/ExtraGui/Earth.gif")
        self.gui.network.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("C:/Users/vkviv/OneDrive/Desktop/Gui/G.U.I Material/ExtraGui/initial.gif")
        self.gui.initatingsystem.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("C:/Users/vkviv/OneDrive/Desktop/Gui/G.U.I Material/ExtraGui/Jarvis_Gui (1).gif")
        self.gui.Jarvis.setMovie(self.gui.label5)
        self.gui.label5.start()

        self.gui.label6 = QtGui.QMovie("C:/Users/vkviv/OneDrive/Desktop/Gui/G.U.I Material/VoiceReg/Ntuks.gif")
        self.gui.label.setMovie(self.gui.label6)
        self.gui.label6.start()

        self.gui.label7 = QtGui.QMovie("C:/Users/vkviv/OneDrive/Desktop/Gui/G.U.I Material/B.G/gyhf.jpg")
        self.gui.Datetime.setMovie(self.gui.label7)
        self.gui.label7.start()

        self.gui.label8 = QtGui.QMovie("C:/Users/vkviv/OneDrive/Desktop/Gui/G.U.I Material/ExtraGui/giphy.gif")
        self.gui.loading.setMovie(self.gui.label8)
        self.gui.label8.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()

    def showTimeLive(Self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        label_time = "Time :" + time
        label_date = "Date :" + date

        Self.gui.Time.setText(label_time)
        Self.gui.Date.setText(label_date)

GuiApp = QApplication(sys.argv)
candy_gui = Gui_start()
candy_gui.show()
sys.exit(GuiApp.exec_())