import threading
import socket
import multiprocessing

import basic_decryptor

MAX_LEN = 128


class Client:
    def __init__(self, ip, port):
        self.client = socket.socket()
        self.client.connect((ip, port))

        data_l = self.client.recv(MAX_LEN).decode().split('#')
        self.start = int(data_l[0])
        self.end = int(data_l[1])

        self.enc_data = self.client.recv(MAX_LEN).decode()


    def defineJmp(self):
        cpu_num = multiprocessing.cpu_count()
        self.jmp = (self.end - self.start)//cpu_num

    def Calculate(self):
        calc = Handle_Calc(self.start, self.enc_data)
        cur = self.start
        thrd_list = []
        while cur < self.end:
            t = threading.Thread(target = Handle_Calc.nextCalc, args = (calc, cur, self.jmp,))
            thrd_list.append(t)
            t.start()




class Handle_Calc:
    def __init__(self,start):
        self.current = start
    def nextCalc(self, start, jmp):
        for num in range(start, start + jmp):
            st = str(num)
            worker = basic_decryptor.md5_worker()
            dec = worker.encode(st)
            if dec =





def main():
    client = Client("127.0.0.1", 8080)

    client.defineJmp()







if __name__ == "__main__":
    main()