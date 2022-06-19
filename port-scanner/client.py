from base64 import encode
import socket


def main():
    server = ("localhost", 7777)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)

        while True:
            m = input("Message to server: ")
            bytes = bytearray(m, 'utf-8')
            s.send(bytes)
            data = s.recvfrom(4096)
            if(data):
                print(data)


if __name__ == "__main__":
    main()
