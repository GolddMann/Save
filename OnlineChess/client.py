import socket
import sys
import pygame
import multiprocessing
from pygame.rect import Rect
game_state = []

num_to_figure = {
    0: 'Empty',
    1: 'Rook',
    2: 'Knight',
    3: 'bishop',
    4: 'King',
    5: 'Queen',
    6: 'Pawn',
}

figure_images_part = {
    1: (332, 0, 83, 83),
    2: (249, 0, 83, 83),
    3: (166, 0, 83, 83),
    4: (0, 0, 83, 83),
    5: (83, 0, 83, 83),
    6: (415, 0, 83, 83),
}


color_to_byte = {
    0: 'white',
    1: 'black'
}


def getBoardData(read, write):
    client = read.get()
    data = client.recv(4096)
    write.put(data)


def print_board(screen):
    pass


def place_figures(board, screen):
    for piece in range(0, len(board), 2):
        p = int(board[piece:piece+2])
        if p == 0:
            continue
        else:
            piece_image = None
            if p > 10:
                piece_image = pygame.image.load('figures.png')
            else:
                piece_image = pygame.image.load('figures.png')

            piece_rect = Rect((piece % 8) * 83, (piece // 8)*83, 83, 83)
            screen.blit(piece_image, piece_rect)


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
        decoded_data = data.decode('utf-8')

        if(data):
            if(decoded_data[0] == 'b'):
                x, y = 0, 0
                cwidth, cheight = 100, 100
                BLACK = (0, 0, 0)
                WHITE = (255, 255, 255)
                cur_white = True
                for i in range(8):
                    cur_white = ((i+1) & 1)
                    for j in range(8):
                        rect = Rect(i*cwidth, j * cheight, cwidth, cheight)
                        color = BLACK
                        if(cur_white):
                            color = WHITE
                        pygame.draw.rect(screen, color, rect)
                        cur_white = not cur_white
                place_figures(decoded_data[1:131], screen)

            else:
                print(decoded_data)

        pygame.display.update()


if __name__ == "__main__":
    main()
