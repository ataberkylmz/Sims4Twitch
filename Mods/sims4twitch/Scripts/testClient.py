import socket
import threading
import config

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = config.host
        self.port = config.port
        self.isConnected = False

    def connect(self, output):
        try:
            self.socket.connect((self.host, self.port))
            self.isConnected = True
            output("Connected to {}".format(config.host))
        except:
            output("Connection failed!")
            self.isConnected = False

    def send(self):
        if self.isConnected == True:
            self.socket.sendall(b'Socket test')

    def listen(self):
        if self.isConnected == True:
            data = self.socket.recv(1024)
            return data
    
    '''def listen_socket(self):
        threading.Thread(target=self.listen, args=[]).start()

    def send_message(self):
        threading.Thread(target=self.send, args=[]).start()

    def listen(self):
        global command

    def send(self):
        global message
        self.socket.sendall(b'Hello, world')
        data = s.recv(1024)
    '''

