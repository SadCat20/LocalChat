import socket
import threading
##########################################
def send_message():
    while True:
        my_msg = input(str())
        if my_msg == 'close':
            conn.send(my_msg)
            break
        conn.send(my_msg.encode())
        my_msg = ''
    conn.close()

def get_message():
    while True :
        msg = conn.recv(1024).decode()
        if msg != '':
            if msg == 'close':
                break
            print(addr[0], ' send: ', msg)
            msg = ''
    conn.close()
##########################################
if __name__ == "__main__":
    sk = socket.socket()
    ad = str(socket.gethostbyname_ex(socket.gethostname())[2][1])
    print('My server IP: ', ad)
    sk.bind((ad, 8080))
    print('Server start')
    sk.listen(1)
    conn, addr = sk.accept()
    print('Connect: ', str(addr[0]))

    get_msg = threading.Thread(target=get_message, name='get', args=())
    send_msg = threading.Thread(target=send_message, name='send', args=())

    get_msg.start()
    send_msg.start()
    get_msg.join()
    send_msg.join()