import threading
import socket
import multiprocessing
import basic_decryptor

MAX_LEN = 128

def handle_client(client, start, finish):
    client.send((str(start) + "#" + str(finish)).encode())
    res = client.recv(128)



def main():
    server = socket.socket()
    server.bind(("127.0.0.1", 8080))
    server.listen(1)
    count = 0
    th_list = []
    jmp = 10 ** 5
    while count * jmp < 10 ** 10:
        client, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(client, count * jmp, (count + 1) * jmp))
        t.daemon = True
        t.start()
        th_list.append(t)

        count += 1


if __name__ == "__main__":
    main()