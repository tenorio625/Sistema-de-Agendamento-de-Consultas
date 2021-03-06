# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GITHUB\agendamento\telas\CONSULTAS.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 452)
        MainWindow.setStyleSheet("background-color: rgb(177, 177, 177);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pacientes = QtWidgets.QPushButton(self.centralwidget)
        self.pacientes.setGeometry(QtCore.QRect(280, 30, 191, 41))
        self.pacientes.setObjectName("pacientes")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-200, -10, 1571, 101))
        self.label.setStyleSheet("background-color: rgb(255, 220, 114);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.consultas = QtWidgets.QPushButton(self.centralwidget)
        self.consultas.setGeometry(QtCore.QRect(40, 30, 191, 41))
        self.consultas.setObjectName("consultas")
        self.tabela_consultas = QtWidgets.QTableWidget(self.centralwidget)
        self.tabela_consultas.setGeometry(QtCore.QRect(60, 110, 541, 241))
        self.tabela_consultas.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_consultas.setObjectName("tabela_consultas")
        self.tabela_consultas.setColumnCount(3)
        self.tabela_consultas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_consultas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_consultas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_consultas.setHorizontalHeaderItem(2, item)
        self.tabela_consultas.horizontalHeader().setVisible(False)
        self.tabela_consultas.horizontalHeader().setCascadingSectionResizes(False)
        self.tabela_consultas.horizontalHeader().setDefaultSectionSize(180)
        self.tabela_consultas.horizontalHeader().setHighlightSections(True)
        self.tabela_consultas.horizontalHeader().setSortIndicatorShown(False)
        self.tabela_consultas.horizontalHeader().setStretchLastSection(False)
        self.tabela_consultas.verticalHeader().setVisible(False)
        self.tabela_consultas.verticalHeader().setCascadingSectionResizes(False)
        self.tabela_consultas.verticalHeader().setHighlightSections(True)
        self.tabela_consultas.verticalHeader().setSortIndicatorShown(False)
        self.tabela_consultas.verticalHeader().setStretchLastSection(False)
        self.nova_consulta = QtWidgets.QPushButton(self.centralwidget)
        self.nova_consulta.setGeometry(QtCore.QRect(680, 110, 161, 31))
        self.nova_consulta.setObjectName("nova_consulta")
        self.att_consultas = QtWidgets.QPushButton(self.centralwidget)
        self.att_consultas.setGeometry(QtCore.QRect(680, 150, 161, 31))
        self.att_consultas.setObjectName("att_consultas")
        self.excluir_consulta = QtWidgets.QPushButton(self.centralwidget)
        self.excluir_consulta.setGeometry(QtCore.QRect(680, 190, 161, 31))
        self.excluir_consulta.setObjectName("excluir_consulta")
        self.excluir_duplicadas = QtWidgets.QPushButton(self.centralwidget)
        self.excluir_duplicadas.setGeometry(QtCore.QRect(680, 260, 161, 31))
        self.excluir_duplicadas.setObjectName("excluir_duplicadas")
        self.label.raise_()
        self.pacientes.raise_()
        self.consultas.raise_()
        self.tabela_consultas.raise_()
        self.nova_consulta.raise_()
        self.att_consultas.raise_()
        self.excluir_consulta.raise_()
        self.excluir_duplicadas.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pacientes.setText(_translate("MainWindow", "Pacientes"))
        self.consultas.setText(_translate("MainWindow", "Consultas"))
        item = self.tabela_consultas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Paciente"))
        item = self.tabela_consultas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tabela_consultas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Horario"))
        self.nova_consulta.setText(_translate("MainWindow", "NOVA CONSULTA"))
        self.att_consultas.setText(_translate("MainWindow", "ATUALIZAR CONSULTA"))
        self.excluir_consulta.setText(_translate("MainWindow", "EXCLUIR CONSULTA"))
        self.excluir_duplicadas.setText(_translate("MainWindow", "EXCLUIR DUPLICADAS"))
