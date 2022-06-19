import socket


def main():
    server = ('localhost', 7777)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(server)
    s.listen()

    clients = []

    while(True):
        sock, addr = s.accept()
        if(sock):
            clients.append((sock, addr))
            print(f"new connection from port: {addr}")
            bytes = bytearray('hello', 'utf-8')

            for c in clients:
                sock.sendto(bytes, c[1])

        data, addr = s.recv(4096)
        if(data):
            print(f'From {addr}: {data}')


if __name__ == "__main__":
    main()
