import socket
import threading


##########################################

class Server:
    def __init__(self):
        self.client_count = 0
        self.conn_flag = False
        self.sk = socket.socket()
        self.client_name = []
        self.conn_lst = {}
        self.my_addr = str(socket.gethostbyname_ex(socket.gethostname())[2][1])
        print(self.my_addr)

    def start_server(self):
        self.sk.bind((self.my_addr, 8080))
        print("Server start on: {}:{}".format(self.my_addr, 8080))

    def server_listener(self):
        for i in range(0, 100):
            self.sk.listen()
            conn, ad = self.sk.accept()
            name = conn.recv(1024).decode()
            self.client_name = self.client_name + [name]
            self.conn_lst[name] = [conn, ad]
            self.conn_flag = True
            self.client_count += 1
            print(self.client_name[i], self.conn_lst[name])
            print(i, self.client_count)

    def get_message(self):
        msg = ''
        while True:
            for i in range(0, self.client_count):
                try:
                    msg = self.conn_lst[self.client_name[i]][0].recv(1024).decode()
                    if not (msg.endswith('edp') and msg.startswith('edp')) and msg != '':
                        msg = ''.join(msg.replace('edp', ''))
                        for j in range(0, self.client_count):
                            self.conn_lst[self.client_name[j]][0].send(
                                '{}: {}'.format(str(self.client_name[i]), str(msg)).encode())
                        msg = ''
                except:
                    pass


##########################################

if __name__ == "__main__":
    server = Server()
    server.start_server()

    get_msg = threading.Thread(target=server.get_message, name='get', args=())
    listener = threading.Thread(target=server.server_listener, name='listener', args=())

    get_msg.start()
    listener.start()
    get_msg.join()
    listener.join()
