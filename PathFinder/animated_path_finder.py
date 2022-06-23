
import pygame

colors = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'BLUE': (0, 0, 255)
}


class Maze:
    def __init__(self, maze, start, goal):
        self.maze = maze
        self.start = start
        self.goal = goal

    def solve_dfs(self):
        self.dfs(self.start)

    def solve_bfs(self):
        self.bfs(self.start)

    def dfs(self, cur):
        pass

    def bfs(self, cur):
        queue = [cur]
        used = [False]*len(self.maze)
        while len(queue):
            pop = queue[0]
            if not used[pop]:
                pass


def draw_grid(screen, width, height, num_in_row, maze):
    cell_size_width = width//num_in_row
    line_width = 1
    for i in range(num_in_row):
        pygame.draw.line(
            screen, colors['WHITE'], (0, cell_size_width*(1 + i)), (width, cell_size_width*(1 + i)), line_width)

    for i in range(num_in_row):
        pygame.draw.line(
            screen, colors['WHITE'], (cell_size_width*(1 + i), 0), (cell_size_width*(1 + i), height), line_width)

    for i in range(num_in_row):
        for j in range(num_in_row):
            if maze[i][j] == 1:
                rect = pygame.rect.Rect(
                    j*cell_size_width + line_width, i*cell_size_width + line_width, cell_size_width-2*line_width, cell_size_width-2*line_width)
                pygame.draw.rect(screen, colors['BLUE'], rect)


def main():
    pygame.init()
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    cell_num_in_row = 10
    cell_size = width//cell_num_in_row

    maze = [[0]*cell_num_in_row]*cell_num_in_row

    mouse_pressed = False

    while True:
        for event in pygame.event.get():
            if event.type == 768 and event.__dict__["key"] == 27 or event.type == 256:
                pygame.quit()
                exit()

            if event.type == 1025 and event.__dict__["button"] == 1 or mouse_pressed:
                mouse_pressed = True
                x, y = pygame.mouse.get_pos()

                maze_row = y//cell_size
                maze_column = x//cell_size

                if maze[maze_row][maze_column] == 0:
                    maze[maze_row][maze_column] = 1

            if event.type == 1026:

                for i in range(cell_num_in_row):
                    for j in range(cell_num_in_row):
                        print(maze[i][j], end=' ')
                    print('')
                print('\n')

                mouse_pressed = False

        screen.fill(colors['BLACK'])

        draw_grid(screen, width, height, cell_num_in_row, maze)

        pygame.display.update()


if __name__ == '__main__':
    main()
