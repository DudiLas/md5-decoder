import threading
import socket
import multiprocessing
MAX_LEN = 128


class Client:
    def __init__(self, ip, port):
        self.client = socket.socket()
        self.client.connect((ip, port))

        data_l = self.client.recv(MAX_LEN).decode().split('#')
        self.start = int(data_l[0])
        self.end = int(data_l[1])


    def defineJmp(self):
        cpu_num = multiprocessing.cpu_count()
        self.jmp = (self.end - self.start)//cpu_num

    def Calculate(self):
        t = threading.Thread(target = )



class Handle_Calc:
    def __init__(self,start):
        self.current = start
    def nextCalc(self, jmp):
        pass







    def calc(client):
        pass

def main():
    client = Client("127.0.0.1", 8080)

    client.defineJmp()







if __name__ == "__main__":
    main()