import socket
from time import sleep
import random

num_to_figure = {
    0: 'Empty',
    1: 'Rook',
    2: 'Knight',
    3: 'bishop',
    4: 'Queen',
    5: 'King',
    6: 'Pawn',
}

color_to_byte = {
    0: 'white',
    1: 'black'
}


def check_win(board):
    pass


def change_board(current_board, data):
    current_board[int(data[:2])][int(data[2:4])] = int(data[4:6])
    current_board[int(data[6:8])][int(data[8:10])] = int(data[10:12])


def main():
    server_address = ('localhost', 7777)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(server_address)
    server.listen(2)

    connections = {}
    client_addresses = []

    initial_board = [[17, 18, 19, 20, 21, 19, 18, 17],
                     [22, 22, 22, 22, 22, 22, 22, 22],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [6, 6, 6, 6, 6, 6, 6, 6],
                     [1, 2, 3, 4, 5, 3, 2, 1]]

    current_board = initial_board[::]

    while True:
        sock, addr = server.accept()

        if(sock and addr):
            client_addresses.append(addr)
            connections[addr] = [sock]

        data = sock.recv(20)

        connections[addr].append(data)

        if(len(connections) == 1):
            connections[addr][0].send(
                bytearray(b'Waiting for second player...'))

        if(len(connections) == 2):
            names = [connections[client_addresses[0]]
                     [1], connections[client_addresses[1]][1]]

            addrs = [client_addresses[0], client_addresses[1]]

            socks = [connections[client_addresses[0]]
                     [0], connections[client_addresses[1]][0]]

            socks[0].send(bytearray(
                (f'You are playing against {names[1]}').encode('ascii')))

            socks[1].send(bytearray(
                (f'You are playing against {names[0]}').encode('ascii')))

            for i in range(5, 0, -1):
                for j in range(2):
                    socks[j].send(bytearray(
                        (f'Game is starting in {i}').encode('ascii')))
                sleep(1)

            current_player = random.randint(0, 1)
            first_player_name = names[current_player]

            for i in range(2):
                socks[i].send(bytearray(
                    (f'{names[current_player]} moves first!\n').encode("ascii")))

            while True:
                board = ""

                for i in range(8):
                    for j in range(8):
                        figure = ''
                        if(len(str(current_board[i][j])) == 2):
                            figure = str(current_board[i][j])
                        else:
                            figure = '0' + str(current_board[i][j])
                        board += figure

                board_str = "b" + board

                if(names[current_player] == first_player_name):
                    board_str += "nr"

                socks[current_player].send(
                    bytearray(board_str.encode('ascii')))

                board_str = "b" + board + "rr"

                socks[(current_player+1) % 2].send(
                    bytearray(board_str.encode('ascii')))

                data = socks[current_player].recv(4096)

                data = data.decode('utf-8')

                current_board = change_board(current_board, data)

                if(check_win(current_board) == 1):
                    for j in range(2):
                        socks[i].send(current_board)

                sock[(current_player+1) %
                     2].send(bytearray(current_board.encode('utf-8')))

                current_player = (current_player+1) % 2


if __name__ == "__main__":
    main()
