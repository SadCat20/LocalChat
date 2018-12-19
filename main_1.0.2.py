import sys
import os
import threading

import time
from PyQt5 import QtWidgets
from msg import msg_design
import socket


class MainApp(QtWidgets.QMainWindow, msg_design.Ui_MainWindow):
    def __init__(self):
        self.addr = []
        self.name = "NoName"
        self.first_conn = True
        super().__init__()
        self.sk = socket.socket()
        self.sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.setupUi(self)
        self.addr_button.clicked.connect(self.new_addr)
        self.name_button.clicked.connect(self.get_name)
        self.send_msg.clicked.connect(self.send_message)
        self.threads()

    def threads(self):
        edp_thread = threading.Thread(target=self.send_zero)
        get_msg_thread = threading.Thread(target=self.get_message)
        edp_thread.start()
        get_msg_thread.start()

    def send_zero(self):
        while True:
            if not self.first_conn:
                self.sk.send('edp'.encode())  # send empty data package
                time.sleep(0.1)

    def get_message(self):
        while True:
            if not self.first_conn:
                another_msg = self.sk.recv(1024).decode()
                self.another_msg.append(str(another_msg).replace('b', ''))
                another_msg = ''

    def send_message(self):
        self.msg = self.your_msg.toPlainText()
        self.sk.send(self.msg.encode())
        self.your_msg.clear()

    def new_addr(self):
        self.addr = str(self.addr_edit.text()).split(':')
        if self.first_conn:
            self.sk.connect(((str(self.addr[0])), int(self.addr[1])))
            self.sk.send(self.name.encode())
            self.first_conn = False
        else:
            self.sk.connect(((str(self.addr[0])), int(self.addr[1])))
            self.sk.send(self.name.encode())
        self.another_msg.append("I connected")

    def get_name(self):
        self.name = str(self.name_edit.text())


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
