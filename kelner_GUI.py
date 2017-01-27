# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kelner.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# COPYRIGHT @ AGATA BUSZCZAK 2017

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self):

        self.gender = ''
        self.amount = 0
        self.stat = 'talk'

        self.clientDialog = ''
        self.waiterDialog = 'Dzień dobry!'

        self.foodText = ''
        self.drinksText = ''


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
        else:
            self.gender = 'male'




        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

########### STATS FUNCTIONS ################################################################################################

    #dodać więcej statusów? jakoś zrobić oczekiwanie na posiłek czy coś? jakieś propozycje???
    def change_stat(self):
        if self.stat == 'talk':
            self.stat = 'eating'
            self.textCurrentAction.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">posiłek</span></p></body></html>")

        else:
            self.stat = 'talk'
            self.textCurrentAction.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">rozmowa z kelnerem</span></p></body></html>")

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
        self.textCurrentAction.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">INTERAKCJA ZAKOŃCZONA: WYJDŹ Z RESTAURACJI</span></p></body></html>")



####### BOXES UPDATES ####################################### update of status box is in status change lol whateva, you can move updateAmpunt somewhere too depends how much you'll expand it

    def updateAmount(self, add):
        self.amount += add #jak w funkcji liczenia aktualnej sumy jest coś jeszcze to dopisz do tej funkcji, a jak chcesz mieć własną funkcje która liczy to usuń ta linijke i argument add tej funkcji
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


    #def talk(self):
        ### ROZMMOWA ###
        ### to co właśnie powiedział klient jest wprowadzane do zmiennej self.clientDialog (za każdym razem jest tam tylko to co powiedział ostatnio)
        ##gdy kelner coś powie:
        # ustawić self.waiterDialog = to_co_mówi - żeby było w stringu to co mówi/ma sie wyswietlać i wywołać self.waiterSays()
        ### gdy kelner odchodzi trzeba wywołać funkcje change_stat()
        ### gdy kelner przynosi posiłek trzeba wywołać updateFood() / udpadeDrinks()

################################################################################

########## BUTTONS FUNCTIONS ###############################################################################################

    def say(self):
        if self.stat != 'END':
            self.clientDialog = self.clientLineEdit.text()
            self.clientSays()
            self.clientLineEdit.clear()

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
            # if:
                self.setAmount(0)
            ## kelner mówi dziękuję za zapłate + pożegnanie?
                self.endInteraction()
            ## po zapłacie kończy się interakcja i jedyne co można w aplikacji zrobić to z niej wyjść :D

    def call(self):
        if self.stat != 'END':
            if self.stat == 'eating':
                #kelner mówi coś w stylu co moge dla pani/pana zrobić (wraca do rozmowy)
                self.change_stat()

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
        self.callButton.setText(_translate("Form", "Zawołaj kelnera"))
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

