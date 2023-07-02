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
import json
import random
from PyQt5 import QtCore
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("Chatbot\intents.json", 'r') as json_data:
    intents = json.load(json_data)


FILE = "TrainData.pth"
data = torch.load(FILE)


input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# -------------------------

Name = "Hinata"

from Neck.Listen import Listen
from Neck.Speak import Say
from Task import NonInputExecution
from Task import InputExecution

def Main():

    sentence = Listen()
    result = str(sentence)

    if sentence == "goodbye":
        Say("See you later Sir! Take care!")
        exit()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    NonInputExecution(reply)

                elif "date" in reply:
                    NonInputExecution(reply)

                elif "joke" in reply:
                    NonInputExecution(reply)

                elif "TimeTable" in reply:
                    NonInputExecution(reply)

                elif "screenshot" in reply:
                    NonInputExecution(reply)

                elif "Notepad" in reply:
                    NonInputExecution(reply)

                elif "game" in reply:
                    NonInputExecution(reply)

                elif "pause" in reply:
                    NonInputExecution(reply)

                elif "play" in reply:
                    NonInputExecution(reply)

                elif "mute" in reply:
                    NonInputExecution(reply)

                elif "unmute" in reply:
                    NonInputExecution(reply)

                elif "volume up" in reply:
                    NonInputExecution(reply)

                elif "volume down" in reply:
                    NonInputExecution(reply)

                elif "google" in reply:
                    InputExecution(reply, result)

                elif "activate how to do mode" in reply:
                    InputExecution(reply,result)

                elif "open" in reply:
                    InputExecution(reply, result)

                elif "close" in reply:
                    InputExecution(reply, result)

                elif "wikipedia" in reply:
                    InputExecution(reply, result)

                elif "weather-check" in reply:
                    InputExecution(reply, result)

                elif "News" in reply:
                    InputExecution(reply, result)

                elif "write a note" in reply:
                    NonInputExecution(reply)

                elif "youtube" in reply:
                    InputExecution(reply, result)

                elif "send email" in reply:
                    InputExecution(reply, result)

                elif "check email" in reply:
                    InputExecution(reply, result)

                else:
                    Say(reply)

    while True:
     Main()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        Main()

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