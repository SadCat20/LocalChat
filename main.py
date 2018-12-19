import sys
import os
from PyQt5 import QtWidgets
import msg_design
import socket

class MainApp(QtWidgets.QMainWindow, msg_design.Ui_MainWindow):
    def __init__(self):
        self.addr = []
        self.name = ""
        self.first_conn = True
        super().__init__()
        self.sk = socket.socket()
        self.setupUi(self)
        self.addr_button.clicked.connect(self.new_addr)
        self.name_button.clicked.connect(self.get_name)
        self.send_msg.clicked.connect(self.send_message)

    def send_message(self):
        self.msg = self.your_msg.toPlainText()
        print(self.msg)
        self.sk.send(self.msg.encode())

    def new_addr(self):
        self.addr = str(self.addr_edit.text()).split(':')
        self.sk.connect(((str(self.addr[0])), int(self.addr[1])))

    def get_name(self):
        self.name = str(self.name_edit.text())
        print(self.name)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
if __name__ == "__main__":
    main()