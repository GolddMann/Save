import socket
import sys
import pygame
import multiprocessing
from pygame.rect import Rect


def getBoardData(read, write):
    client = read.get()
    data = client.recv(4096)
    write.put(data)


def print_board(screen):
    pass


def place_figures(board, screen):
    pass


def main():
    # pygame display settings
    size = width, height = 800, 800
    pygame.init()
    screen = pygame.display.set_mode(size)

    server_address = ('localhost', 7777)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(server_address)
    except:
        print('Connection error!')

    name = input("Enter your name: ")
    client.send(name.encode('ascii'))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                client.close()
                sys.exit()

        read = multiprocessing.Queue()
        write = multiprocessing.Queue()

        read.put(client)
        p = multiprocessing.Process(target=getBoardData, args=(read, write,))
        p.start()
        data = write.get()

        if(data.decode('utf-8')):
            if(data[0] == "b"):
                x, y = 0, 0
                cwidth, cheight = 100, 100
                BLACK = (0, 0, 0)
                WHITE = (255, 255, 255)
                cur_white = True
                for i in range(8):
                    for j in range(8):
                        rect = Rect(x + i*cwidth, y + j *
                                    cheight, cwidth, cheight)
                        color = BLACK
                        if(cur_white):
                            color = WHITE
                        pygame.draw.rect(screen, color, rect)
                        cur_white = not cur_white
                place_figures(data[1:131], screen)

            else:
                print(data.decode("ascii"))

        pygame.display.update()


if __name__ == "__main__":
    main()
