# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GITHUB\agendamento\telas\MARCAR_CONSULTA.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 259)
        MainWindow.setStyleSheet("background-color: rgb(246, 255, 152);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dados = QtWidgets.QLabel(self.centralwidget)
        self.dados.setGeometry(QtCore.QRect(130, 20, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dados.setFont(font)
        self.dados.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.dados.setObjectName("dados")
        self.c_paciente = QtWidgets.QLineEdit(self.centralwidget)
        self.c_paciente.setGeometry(QtCore.QRect(100, 90, 141, 31))
        self.c_paciente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_paciente.setObjectName("c_paciente")
        self.c_data = QtWidgets.QLineEdit(self.centralwidget)
        self.c_data.setGeometry(QtCore.QRect(350, 90, 141, 31))
        self.c_data.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_data.setObjectName("c_data")
        self.c_hora = QtWidgets.QLineEdit(self.centralwidget)
        self.c_hora.setGeometry(QtCore.QRect(630, 90, 141, 31))
        self.c_hora.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c_hora.setObjectName("c_hora")
        self.botao_marcar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_marcar.setGeometry(QtCore.QRect(350, 190, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.botao_marcar.setFont(font)
        self.botao_marcar.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.botao_marcar.setObjectName("botao_marcar")
        self.aviso = QtWidgets.QLabel(self.centralwidget)
        self.aviso.setGeometry(QtCore.QRect(260, 130, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.aviso.setFont(font)
        self.aviso.setText("")
        self.aviso.setAlignment(QtCore.Qt.AlignCenter)
        self.aviso.setObjectName("aviso")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dados.setText(_translate("MainWindow", "Paciente                                  Data                                         Horario"))
        self.botao_marcar.setText(_translate("MainWindow", "Marcar Consulta"))
