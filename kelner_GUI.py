# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kelner.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# COPYRIGHT @ AGATA BUSZCZAK 2017

from PyQt5 import QtCore, QtGui, QtWidgets
import linecache
import random
import codecs

class Ui_Form(object):
    def __init__(self):

        self.gender = ''
        self.amount = 0
        self.stat = 'talk'

        self.clientDialog = ''
        self.waiterDialog = ''

        self.foodText = ''
        self.drinksText = ''

        ### zmienne rozmowy
        self.liczbajedz = 0
        self.liczbapic = 0
        self.odpowiedzi = ''

        ### flagi

        self.picie = False
        self.jedzenie = False

        self.pnapoj = False
        self.pjedzenie = False

        self.propozycja = False
        self.kontynuuj = False
        self.upewnienie = False
        self.odpowiedz = False
        self.wiecej = False
        self.n = 0
        self.j = 0

        self.powitanie = True #potrzebne na początku dialogu

        self.slownikpropozycji = {"tak":"tak","poprosze":"tak","poproszę":"tak","poprosimy":"tak","dobrze":"tak","spróbuję":"tak","sprobuje":"tak","spróbuje":"tak","okej":"tak",
"dobra":"tak","ok":"tak"}

        self.slownik = {"żurek": "zurek", "żurku": "zurek", "żurkiem": "zurek", "zurek": "zurek", "zurku": "zurek",
               "zurkiem": "zurek",
               "rosół": "rosol", "rosołem": "rosol", "rosol": "rosol", "rosolem": "rosol",
               "krupnik": "krupnik", "krupnika": "krupnik", "krupnikiem": "krupnik", "krupniku": "krupnik",
               "bigos": "bigos", "bigosu": "bigos", "bigosem": "bigos", "bigosie": "bigos",
               "placek": "placek", "placka": "placek", "plackiem": "placek", "placku": "placek",
               "schabowy": "schabowy", "schabowego": "schabowy", "schabowym": "schabowy", "schab":"schabowy",
               "schaba":"schabowy",
               "filet": "filet", "filetu": "filet", "filetem": "filet", "filecie": "filet",
               "spaghetti": "spaghetti",
               "surówki": "surowki", "surówek": "surowki", "surówkom": "surowki", "surówkami": "surowki",
               "surówkach": "surowki", "surówkę": "surowki", "surówką": "surowki",
               "surowki": "surowki", "surowek": "surowki", "surowkom": "surowki", "surowkami": "surowki",
               "surowkach": "surowki", "surówke": "surowki", "surowka": "surowki",
               "ziemniaki": "ziemniaki", "ziemniaków": "ziemniaki", "ziemniakom": "ziemniaki",
               "ziemniakami": "ziemniaki", "ziemniakach": "ziemniaki", "ziemniakow": "ziemniaki",
               "kasza": "kasza", "kaszy": "kasza", "kaszę": "kasza", "kaszą": "kasza", "kasze": "kasza",
               "ryż": "ryz", "ryżu": "ryz", "ryżowi": "ryz", "ryżem": "ryz", "ryz": "ryz", "ryzu": "ryz",
               "ryzowi": "ryz", "ryzem": "ryz",
               "warzywa": "warzywa", "warzyw": "warzywa", "warzywom": "warzywa", "warzywami": "warzywa",
               "warzywach": "warzywa",
               "dorsz": "dorsz", "dorsza": "dorsz", "dorszowi": "dorsz", "dorszem": "dorsz", "dorszu": "dorsz",
               "frytki": "frytki", "frytek": "frytki", "frytkom": "frytki", "frytkami": "frytki", "frytkach": "frytki",
               "cola": "cola", "coli": "cola", "cole": "cola", "colę": "cola", "colą": "cola",
               "pepsi": "pepsi",
               "fanta": "fanta", "fanty": "fanta", "fante": "fanta", "fantę": "fanta", "fantą": "fanta",
               "herbata": "herbata", "herbaty": "herbata", "herbatę": "herbata", "herbate": "herbata",
               "herbatą": "herbata",
               "gazowana": "gaz", "gazowaną": "gaz", "gazowanej": "gaz",
               "niegazowana": "niegaz", "niegazowanej": "niegaz", "niegazowaną": "niegaz",
               "lemoniada": "lemoniada", "lemoniady": "lemoniada", "lemoniadzie": "lemoniada", "lemoniadę": "lemoniada",
               "lemoniadą": "lemoniada", "lemoniade": "lemoniada",
               "proponować": "propozycja", "proponuje": "propozycja", "zaproponuje": "propozycja","zaproponować": "propozycja","propozycji": "propozycja",
               "proponowac": "propozycja","zaproponowac": "propozycja","zaproponujesz":"propozycja","propozycja":"propozycja","zaproponował":"propozycja",
               "proponuj":"propozycja", "poleciłby": "propozycja", "polecenia": "propozycja","poleć": "propozycja", "polecacie":"propozycja",
               "polecić":"propozycja", "proponujecie":"propozycja", "polecasz":"propozycja", "propozycję":"propozycja", "poleca":"propozycja","zaproponowali":"propozycja",
               "jedzenie": "jedzenie", "jedzenia": "jedzenie", "jedzeniu": "jedzenie", "jedzeniem": "jedzenie",
               "danie": "danie", "dania": "danie", "dań": "danie", "dan": "danie",
               "picia": "picie", "picie": "picie", "piciu": "picie", "piciem": "picie",
               "napój": "napoj", "napoj": "napoj", "napoju": "napoj", "napojem": "napoj"
        }

        self.slownikjedzenie = ['zurek', 'rosol', 'krupnik', 'bigos', 'placek', 'schabowy', 'filet', 'spaghetti', 'surowki', 'ziemniaki',
'kasza', 'ryz', 'warzywa', 'dorsz', 'frytki']

        self.slowniknapoje = ['cola', 'pepsi', 'fanta', 'herbata', 'gaz', 'niegaz', 'lemoniada']


    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(946, 783)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 20)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem)
        self.textClient = QtWidgets.QTextBrowser(Form)
        self.textClient.setMinimumSize(QtCore.QSize(500, 100))
        self.textClient.setObjectName("textClient")
        self.verticalLayout_7.addWidget(self.textClient)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem1)
        self.textWaiter = QtWidgets.QTextBrowser(Form)
        self.textWaiter.setMinimumSize(QtCore.QSize(200, 100))
        self.textWaiter.setObjectName("textWaiter")
        self.verticalLayout_7.addWidget(self.textWaiter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, -1)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.clientLineEdit = QtWidgets.QLineEdit(Form)
        self.clientLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.clientLineEdit.setObjectName("clientLineEdit")
        self.horizontalLayout_7.addWidget(self.clientLineEdit)
        self.sayButton = QtWidgets.QPushButton(Form)
        self.sayButton.setMinimumSize(QtCore.QSize(100, 40))
        self.sayButton.setObjectName("sayButton")
        self.horizontalLayout_7.addWidget(self.sayButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.table = QtWidgets.QLabel(Form)
        self.table.setObjectName("table")
        self.verticalLayout_4.addWidget(self.table)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(20, 5, 20, 5)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_13.addWidget(self.label_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(20, 20, 20, 5)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.textFood = QtWidgets.QTextBrowser(Form)
        self.textFood.setMinimumSize(QtCore.QSize(0, 100))
        self.textFood.setObjectName("textFood")
        self.horizontalLayout_11.addWidget(self.textFood)
        self.textDrinks = QtWidgets.QTextBrowser(Form)
        self.textDrinks.setMinimumSize(QtCore.QSize(0, 100))
        self.textDrinks.setObjectName("textDrinks")
        self.horizontalLayout_11.addWidget(self.textDrinks)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(20, 5, 20, 20)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.eatButton = QtWidgets.QPushButton(Form)
        self.eatButton.setMinimumSize(QtCore.QSize(0, 40))
        self.eatButton.setObjectName("eatButton")
        self.horizontalLayout_12.addWidget(self.eatButton)
        self.drinkButton = QtWidgets.QPushButton(Form)
        self.drinkButton.setMinimumSize(QtCore.QSize(0, 40))
        self.drinkButton.setObjectName("drinkButton")
        self.horizontalLayout_12.addWidget(self.drinkButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.verticalLayout_4.addLayout(self.verticalLayout_8)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(10, 25, 10, 25)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setObjectName("label")
        self.verticalLayout_11.addWidget(self.label)
        self.textCurrentAction = QtWidgets.QTextBrowser(Form)
        self.textCurrentAction.setEnabled(True)
        self.textCurrentAction.setMinimumSize(QtCore.QSize(200, 40))
        self.textCurrentAction.setObjectName("textCurrentAction")
        self.verticalLayout_11.addWidget(self.textCurrentAction)
        self.callButton = QtWidgets.QPushButton(Form)
        self.callButton.setMinimumSize(QtCore.QSize(0, 40))
        self.callButton.setObjectName("callButton")
        self.verticalLayout_11.addWidget(self.callButton)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        self.textAmount = QtWidgets.QTextBrowser(Form)
        self.textAmount.setMinimumSize(QtCore.QSize(0, 40))
        self.textAmount.setObjectName("textAmount")
        self.verticalLayout_11.addWidget(self.textAmount)
        self.payButton = QtWidgets.QPushButton(Form)
        self.payButton.setMinimumSize(QtCore.QSize(0, 40))
        self.payButton.setObjectName("payButton")
        self.verticalLayout_11.addWidget(self.payButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 500, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem3)
        self.menuButton = QtWidgets.QPushButton(Form)
        self.menuButton.setMinimumSize(QtCore.QSize(0, 40))
        self.menuButton.setObjectName("menuButton")
        self.verticalLayout_11.addWidget(self.menuButton)
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setMinimumSize(QtCore.QSize(0, 40))
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout_11.addWidget(self.exitButton)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        msg = QtWidgets.QInputDialog()
        msg.setCancelButtonText('Anuluj')
        msg.setLabelText('Wybierz płeć:')
        msg.isComboBoxEditable()
        a=('kobieta','mężczyzna')
        msg.setComboBoxItems(a)
        retval = msg.exec_()
        if retval == 0:
            sys.exit()
        gender = msg.textValue()
        if gender == 'kobieta':
            self.gender = 'female'
            odp = codecs.open('FEMALE.txt', 'r', 'utf-8')
            self.odpowiedzi = odp.read()
            self.odpowiedzi = self.odpowiedzi.split('\n')
            self.waiterDialog = self.odpowiedzi[0]
        else:
            self.gender = 'male'
            odp = codecs.open('MALE.txt', 'r', 'utf-8')
            self.odpowiedzi = odp.read()
            self.odpowiedzi = self.odpowiedzi.split('\n')
            self.waiterDialog = self.odpowiedzi[0]

        with open("MENUJEDZENIE.txt","r") as jedz:
            self.liczbajedz = sum(1 for line in jedz)
        with open("MENUPICIE.txt","r") as jedz:
            self.liczbapic = sum(1 for line in jedz)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

########### STATS FUNCTIONS ################################################################################################


    def setAmount(self, amount):
        self.amount = amount

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender

    def getStat(self):
        return self.stat

    def getAmount(self):
        return self.amount

    def setClientDialog(self, text):
        self.clientDialog = text

    def setWaiterDialog(self, text):
        self.waiterDialog = text

    def getClientDialog(self):
        return self.clientDialog

    def getWaiterdialog(self):
        return self.waiterDialog

    def endInteraction(self):
        self.stat = 'END'
        with open("ZAMOWIENIE.txt","w") as zam:
            zam.seek(0)
            zam.truncate()
        self.textCurrentAction.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">INTERAKCJA ZAKOŃCZONA: WYJDŹ Z RESTAURACJI</span></p></body></html>")
        self.waiterDialog = self.odpowiedzi[9]
        self.waiterSays()


####### BOXES UPDATES ####################################### update of status box is in status change lol whateva, you can move updateAmpunt somewhere too depends how much you'll expand it


    def display_stat(self):
        if self.stat == 'eating':
            self.textCurrentAction.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">posiłek</span></p></body></html>")

        if self.stat == 'talk':
            self.textCurrentAction.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">rozmowa z kelnerem</span></p></body></html>")

        if self.stat == 'wait':
            self.textCurrentAction.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">oczekiwanie na posiłek</span></p></body></html>")

    def updateAmount(self):
        self.textAmount.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">{} zł</span></p></body></html>".format(self.amount))

    def waiterSays(self):
        self.textWaiter.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:300;\">{temp}</span></p></body></html>".format(temp=self.waiterDialog))

    def clientSays(self):
        self.textClient.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-style:italic; color:#707070;\">{temp}</span></p></body></html>".format(temp=self.clientDialog))

    def updateFood(self):
        self.textFood.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">{temp}</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p></body></html>".format(temp=self.foodText))

    def updateDrinks(self):
        self.textDrinks.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">{temp}</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>".format(temp=self.drnksText))


########## ROZMOWA ##########################

    def RandomN(self, only):
        print('random n')
        # Podaje losową pozycje z menu napojów"""
        liczba = random.randint(1, self.liczbapic)
        wiersz = linecache.getline('MENUPICIE.txt', liczba)
        parts = wiersz.split(",")
        propnap = self.odpowiedzi[1].format(liczba, parts[1])
        self.waiterDialog = propnap
        if only:
            self.waiterSays()
            self.kontynuuj = True
        self.n = liczba
        print(self.n)

    def RandomJ(self, only):
        print('random p')
        #"""Podaje losową pozycje z menu posiłków i napojów"""
        liczba = random.randint(1, self.liczbajedz)
        wiersz = linecache.getline('MENUJEDZENIE.txt', liczba)
        parts = wiersz.split(",")
        propjedz = self.odpowiedzi[2].format(liczba, parts[1])
        if not only:
            self.waiterDialog += propjedz
        else:
            self.waiterDialog = propjedz
        self.waiterSays()
        self.kontynuuj = True
        self.j = liczba
        print(self.j)


    def SprawdzOdp(self):
        """Sprawdza czy klient potwierdził propozycję."""
        print('sprawdzanie odpowiedzi')
        x = self.clientDialog                  # wpisz zdanie
        zapisz = x.split()             #pod zmienną 'zapisz' podstawiamy liste slow oddzielonych przecinkiem
        zamowienie = []              # tworzymy tablice 'zmowienie'
        for x in zapisz:             #dodajemy slowa do tablicy 'zamowienie'
            zamowienie.append(x)
        slownik = self.slownikpropozycji
        hasla = []                                  #definiujemy tablice w ktorej znajdowac sie beda slowa kluczowe
        slowo = list(slownik.keys())                  #tworzymy liste w ktorej znajduja sie klucze ze slownika

        for element in zamowienie:
            element = element.lower()                 #zamień wszystkie litery na małe
            if element in slowo:                    # sprawdzamy kazde slowo z zamowienia, jesli znajduje sie ono w slowniku jako klucz to dodajemy je do tablicy z haslami
                    hasla.append(slownik[element])

        if "tak" in hasla:
            print('odp')
            if self.wiecej: #kelner zaputa się co jeszcze podać - nie usuwając już zamówionych produktów zacznie rozmowe na nowo
                print('wiecej w odp tak')
                self.odpowiedz = True
                self.wiecej = False
                self.waiterDialog = self.odpowiedzi[15]
                self.waiterSays()
                #czyszczenie flag:
                self.upewnienie = False
                self.propozycja = False
                self.odpowiedz = False
                self.kontynuuj = False
            else:
                self.odpowiedz = True
                self.kontynuuj = True
                self.updateAmount()
        else:
            if self.wiecej:
                self.Upewnij()
            else:
                self.odpowiedz = False
                self.kontynuuj = False
                self.amount = 0 #jak zamówienie sie nie zgadza to kasuje należność i zaczyna dialog na nowo lol yolo
                self.updateAmount()

    def Upewnij(self):
         if not self.upewnienie:
             if self.odpowiedz or not self.propozycja:
                 print('funkcja Upewnij')
                 s = ", "
                 czylizam = self.odpowiedzi[5]
                 zam = codecs.open("ZAMOWIENIE.txt", "r", "utf-8")
                 zam = zam.read()
                 zam = zam.split("\n")
                 zam.pop()
                 zam = s.join(zam)
                 czylizam = czylizam + " " + zam + "."
                 self.waiterDialog = czylizam
                 self.waiterDialog += ' ' + self.odpowiedzi[6]
                 self.waiterSays()
                 self.upewnienie = True
                 self.kontynuuj = True
             else:
                 self.wypowiedzKelneraProponowanie()

         else:
             print('funkcja upewnij: kontynuacja')
             if self.odpowiedz: # jak zwróci wynik true to pyta sie czy cos jeszcze
                 if not self.wiecej:
                    print('czy cos wiecej')
                    self.waiterDialog = self.odpowiedzi[14]
                    self.waiterSays()
                    self.wiecej = True
                 else: #kelner przynosi zamówienie i odchodzi - status zmienia się na jedzenie - jesli juz nie chcemy nic wiecej
                     print('not self.wiecej')
                     self.waiterDialog = self.odpowiedzi[13]
                     print(self.waiterDialog)
                     self.waiterSays()
                     self.stat = 'eating'
                     self.display_stat()
                     self.updateFood()
                     self.updateDrinks()
                     #czyszczenie flag:
                     self.upewnienie = False
                     self.propozycja = False
                     self.odpowiedz = False
                     self.kontynuuj = False
                     with open("ZAMOWIENIE.txt","w") as zam:
                        zam.seek(0)
                        zam.truncate()
                     with open("jedzenie.txt","w") as zam:
                        zam.seek(0)
                        zam.truncate()
                     with open("napoj.txt","w") as zam:
                        zam.seek(0)
                        zam.truncate()

             else: # kelner pyta się na nowo co w takim razie chce sie zamówić, przez co klient znowu musi cos powiedzieć (tak jakby rozpoczyna rozmowe na nowo, a nie od razu proponuje coś innego)
                 #czyszczenie flag
                 self.upewnienie = False
                 self.propozycja = False
                 self.kontynuuj = False
                 self.odpowiedz = False
                 with open("ZAMOWIENIE.txt","w") as zam:
                    zam.seek(0)
                    zam.truncate()
                 self.amount = 0
                 self.foodText = ''
                 self.drinksText = ''
                 self.waiterDialog = self.odpowiedzi[11]
                 self.waiterSays()

    def wypowiedzKelneraProponowanie(self):

        if not self.kontynuuj:
            print('proponowanie: started')
            self.n = 0
            self.j = 0

            if self.pnapoj:
                print('if dziala')
                if self.pjedzenie:
                    stat = False
                    print('jedzenie: ', stat)
                else:
                    stat = True
                    print(stat)
                self.RandomN(stat)
                self.RandomJ(stat)
            else:
                if self.pjedzenie:
                    self.RandomJ(True)

        else:

            if self.n != 0:
                wiersz = linecache.getline('MENUPICIE.txt', self.n)
                parts = wiersz.split(",")
                with codecs.open("ZAMOWIENIE.txt","a","utf-8") as zam:
                    zam.write(parts[1] + "\n")
                self.amount += float(parts[2])

            if self.j != 0:
                wiersz = linecache.getline('MENUJEDZENIE.txt', self.j)
                parts = wiersz.split(",")
                with codecs.open("ZAMOWIENIE.txt", "a","utf-8") as zam:
                    zam.write(parts[1] + "\n")
                self.amount += float(parts[2])
            self.Upewnij()


    def wypowiedzKlienta(self):
        print('funkcja wypowiedzKlienta')

        x = self.clientDialog  # wpisz zdanie
        zapisz = x.split()  # pod zmienną 'zapisz' podstawiamy liste slow oddzielonych przecinkiem
        zamowienie = []  # tworzymy tablice 'zmowienie'
        for x in zapisz:  # dodajemy slowa do tablicy 'zamowienie'
            zamowienie.append(x)
        slownik = self.slownik
        hasla = []  # definiujemy tablice w ktorej znajdowac sie beda slowa kluczowe
        slowo = list(slownik.keys())  # tworzymy liste w ktorej znajduja sie klucze ze slownika
        for element in zamowienie:
            element = element.lower()  # zamień wszystkie litery na małe
            if element in slowo:  # sprawdzamy kazde slowo z zamowienia, jesli znajduje sie ono w slowniku jako klucz to dodajemy je do tablicy z haslami
                hasla.append(slownik[element])

        self.propozycja = False
        if "propozycja" in hasla:  # klient zażyczył sobie propozycji
            self.propozycja = True
            print(self.propozycja)
            if "picie" in hasla or "napoj" in hasla:
                print('picie')
                self.pnapoj = True
            elif "danie" in hasla or "jedzenie" in hasla:
                print('jedzenie')
                self.pjedzenie = True
            else:
                print('picie i jedzenie')
                self.pnapoj = True
                self.pjedzenie = True
            self.wypowiedzKelneraProponowanie()

        else:
            print('konkret')
            self.picie = False
            n = open('napoj.txt', 'a')
            napoje = self.slowniknapoje
            for haslo in hasla:
                if haslo in napoje:
                    self.picie = True
                    n.write(haslo + '\n')
                    self.drinksText += haslo + ', '
            n.close()

            self.jedzenie = False
            j = open('jedzenie.txt', 'a')
            danie = self.slownikjedzenie
            for haslo in hasla:
                if haslo in danie:
                    self.jedzenie = True
                    j.write(haslo + '\n')
                    self.foodText += haslo + ', '
            j.close()

            if not self.wiecej:
                with open("ZAMOWIENIE.txt", "w") as zam:
                    zam.seek(0)
                    zam.truncate()

            with open("MENUPICIE.txt", "r") as zamowienie, open("napoj.txt", "r") as picie, open("ZAMOWIENIE.txt","a") as ostat:
                picie = [line.rstrip('\n') for line in picie]
                for line in zamowienie:
                    if any(pic in line for pic in picie):
                        skos = line.split(",")
                        ostat.write(skos[1]+"\n")
                        self.amount += float(skos[2])

            with open("MENUJEDZENIE.txt", "r") as zamowienie, open("jedzenie.txt", "r") as jedzenie, open("ZAMOWIENIE.txt","a") as ostat:
                jedzenie = [line.rstrip('\n') for line in jedzenie]
                for line in zamowienie:
                    if any(pic in line for pic in jedzenie):
                        skos = line.split(",")
                        ostat.write(skos[1]+"\n")
                        self.amount += float(skos[2])

            if not self.picie and not self.jedzenie: # klient nie odpowiedział na pytanie
                self.waiterDialog = self.odpowiedzi[12]
                self.waiterSays()
            else:
                print('klient odpowiedzial na pytanie')
                self.Upewnij()


########## BUTTONS FUNCTIONS ###############################################################################################

    def say(self):
        if self.stat != 'END' and self.stat != 'eating':
            self.clientDialog = self.clientLineEdit.text()
            self.clientSays()
            self.clientLineEdit.clear()
            if self.powitanie: # tylko na samym początku: klient może napisac cokolwiek (w założeniu się przywita) a nastepnie kelner pyta sie co podać
                self.waiterDialog = self.odpowiedzi[10]
                self.waiterSays()
                self.powitanie = False
            else:
                if self.wiecej:
                    self.SprawdzOdp()
                else:
                    if self.kontynuuj: #sprawdza czy jesteśmy w trakcie proponowania (wypowiedź jest odp twierdzącą/przeczącą)
                        if self.upewnienie:
                            self.SprawdzOdp()
                            self.Upewnij()
                        else:
                            print('SPR CZY PRZYJMUJESZ PROPOZYCJE')
                            if self.propozycja:
                                self.SprawdzOdp()
                                print(self.odpowiedz)
                                print('self.n: ', self.n, ' self.j: ', self.j)
                                self.wypowiedzKelneraProponowanie()
                    else:
                        if not self.propozycja:
                            print('wyp klienta')
                            self.wypowiedzKlienta()



    def eat(self):
        if self.stat != 'END':
            self.textFood.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p></body></html>")


    def drink(self):
        if self.stat != 'END':
            self.textDrinks.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>")


    def pay(self):
        if self.stat != 'END':
            if self.stat == 'pay':
                self.setAmount(0)
                self.updateAmount()
                self.waiterDialog = self.odpowiedzi[9]
                self.waiterSays()
                self.endInteraction()

    def call(self):
        if self.stat != 'END':
            if self.stat == 'eating':
                self.stat = 'talk'
                self.display_stat()
                self.waiterDialog = self.odpowiedzi[8].format(self.amount)
                self.waiterSays()
                self.stat = 'pay'

    def menu(self):
        print('wip')
        ### STILL GOTTA DO IT BUT THAT DOEASN'T CONNECT TO ANYTHING SO LATER

    def exit(self):
        if self.amount == 0:
            sys.exit()


############################################################################################################################


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "KELNER"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">..:: QUIZNAK ::..</span></p></body></html>"))
        self.textClient.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-style:italic; color:#707070;\">{temp}</span></p></body></html>".format(temp=self.clientDialog)))
        self.textWaiter.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
#"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:300;\">{temp} </span></p></body></html>".format(temp=self.waiterDialog)))
        self.sayButton.setText(_translate("Form", "Powiedz"))
        self.sayButton.clicked.connect(self.say)
        self.clientLineEdit.returnPressed.connect(self.say)
        self.table.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">..:: Stolik ::..</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Twoje jedzenie:</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Twoje napoje:</span></p></body></html>"))
        self.textFood.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p></body></html>"))
        self.textDrinks.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"></span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.eatButton.setText(_translate("Form", "Zjedz"))
        self.eatButton.clicked.connect(self.eat)
        self.drinkButton.setText(_translate("Form", "Wypij"))
        self.drinkButton.clicked.connect(self.drink)
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Wykonywana czynność:</span></p></body></html>"))
        self.textCurrentAction.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">rozmowa z kelnerem</span></p></body></html>"))
        self.callButton.setText(_translate("Form", "Poproś o rachunek"))
        self.callButton.clicked.connect(self.call)
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Suma do zaplacenia:</span></p></body></html>"))
        self.textAmount.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> 0 zł</span></p></body></html>"))
        self.payButton.setText(_translate("Form", "Zapłać"))
        self.payButton.clicked.connect(self.pay)
        self.menuButton.setText(_translate("Form", "Wyświetl menu"))
        self.menuButton.clicked.connect(self.menu)
        self.exitButton.setText(_translate("Form", "Wyjdź z restauracji"))
        self.exitButton.clicked.connect(self.exit)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

