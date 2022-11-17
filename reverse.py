import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname('sgfl.xyz')
        self.port = 2002
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server, self.port))

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    #recieve message from server
    def recieve_from_server(self):
        while(True):
            self.data = ''
            self.data = self.socket.recv(1024)
            self.data = self.data.decode('UTF-8')
            self.data.strip()
            if (self.data != ''):
                print(self.data)
                break
        return self.data[::-1]

    #send message to server
    def send_to_server(self, message):
        self.socket.sendall(str.encode(message))

def main():
        net = Network()
        net.recieve_from_server()
        msg = net.recieve_from_server()
        print(msg)
        msg2 = msg[::-1]
        print(msg2)
        msg.strip()
        net.send_to_server(msg)
        net.recieve_from_server()
main()