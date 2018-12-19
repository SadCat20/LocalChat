# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/users/user/Desktop/test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.another_msg = QtWidgets.QTextEdit(self.groupBox)
        self.another_msg.setObjectName("another_msg")
        self.verticalLayout.addWidget(self.another_msg)
        self.your_msg = QtWidgets.QTextEdit(self.groupBox)
        self.your_msg.setObjectName("your_msg")
        self.verticalLayout.addWidget(self.your_msg)
        self.send_msg = QtWidgets.QPushButton(self.groupBox)
        self.send_msg.setObjectName("send_msg")
        self.verticalLayout.addWidget(self.send_msg)
        self.send_msg.raise_()
        self.your_msg.raise_()
        self.another_msg.raise_()
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addr_edit = QtWidgets.QLineEdit(self.groupBox_2)
        self.addr_edit.setObjectName("addr_edit")
        self.verticalLayout_2.addWidget(self.addr_edit)
        self.addr_button = QtWidgets.QPushButton(self.groupBox_2)
        self.addr_button.setObjectName("addr_button")
        self.verticalLayout_2.addWidget(self.addr_button)
        self.name_edit = QtWidgets.QLineEdit(self.groupBox_2)
        self.name_edit.setObjectName("name_edit")
        self.verticalLayout_2.addWidget(self.name_edit)
        self.name_button = QtWidgets.QPushButton(self.groupBox_2)
        self.name_button.setObjectName("name_button")
        self.verticalLayout_2.addWidget(self.name_button)
        self.horizontalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Сообщения"))
        self.send_msg.setText(_translate("MainWindow", "Отправить сообщение"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Настройки"))
        self.addr_edit.setText(_translate("MainWindow", "Адрес"))
        self.addr_button.setText(_translate("MainWindow", "Подтвердить адрес"))
        self.name_edit.setText(_translate("MainWindow", "Ваше имя"))
        self.name_button.setText(_translate("MainWindow", "Подтвердить имя"))
