from turtle import update
import pygame

COLOR1 = (150, 255, 50)
COLOR2 = (100, 0, 200)
COLOR3 = (100, 0, 0)


def update_pos(object):
    object.x += 1
    object.y += 1


def draw_triangle(screen, t, d):
    if d < 0:
        return
    else:
        triangle = ((t[0][0], t[0][1]), (t[1][0], t[1][1]), (t[2][0], t[2][1]))
        pygame.draw.polygon(screen, COLOR1, triangle)
        t1 = ((t[0][0], t[1][1]), (t[0][0] + (t[2][0]-t[0][0])/2, t[1][1] + (t[2][0]-t[0][0]) /
              2), (t[0][0] - (t[2][0]-t[0][0])/2, t[1][1] + (t[2][0]-t[0][0])/2))
        t2 = ((t[0][0] - (t[2][0]-t[0][0])/2, t[0][1]), (t[0][0] + (t[2][0]-t[0][0])/2, t[0][1] + (t[2][0]-t[0][0]) /
              2), (t[0][0] + (t[2][0]-t[0][0]), t[0][1] + (t[2][0]-t[0][0]) /
              2))
        t3 = ((t[0][0] + (t[2][0]-t[0][0])/2, t[0][1]), (t[0][0] - (t[2][0]-t[0][0])/2, t[0][1] + (t[2][0]-t[0][0]) /
              2), (t[0][0] - (t[2][0]-t[0][0]), t[0][1] + (t[2][0]-t[0][0]) /
              2))
        draw_triangle(screen, t1, depth-1)
        draw_triangle(screen, t2, depth-1)
        draw_triangle(screen, t3, depth-1)


if __name__ == "__main__":
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)

    depth = 1

    x, y, w, h = 40, 40, 40, 40
    rect = pygame.Rect(x, y, w, h)

    basic_triangle = ((w/2, h - h/10), (w/10, h/10), (w - w/10, h/10))
    full_triangle = ((w/2, ))

    while True:
        for event in pygame.event.get():
            if(event.__dict__.get('key') == 27):
                pygame.quit()
                exit(0)
        screen.fill(COLOR2)
        pygame.draw.polygon(screen, COLOR3, basic_triangle)
        draw_triangle(screen, basic_triangle, depth)
        update_pos(rect)
        pygame.display.update()
