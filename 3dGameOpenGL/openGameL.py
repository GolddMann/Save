from OpenGL.GL import *
from OpenGL.GLU import *
from math import sqrt
import pygame
from pygame.locals import *

verti = [(
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)]

cubes = [(
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)]


def Cube():
    glBegin(GL_LINES)
    for cube in range(len(cubes)):
        for edge in cubes[cube]:
            for vertex in edge:
                glVertex3fv(verti[cube][vertex])

    for i in range(len(verti[0])):
        for j in range(len(verti) - 1):
            glVertex3fv(verti[j][i])
            glVertex3fv(verti[j+1][i])
            j += 1

    glEnd()


def generates_cubes(n):
    temp_cube = cubes[0]
    temp_vert = verti[0]

    for i in range(1, n):
        vertexes = []
        for edge in temp_vert:
            vertexes.append((edge[0], edge[1] + i*2, edge[2]))
        verti.append(tuple(vertexes))

        cubes.append(temp_cube)


def main():
    pygame.init()
    display = (900, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(70, (display[0] / display[1]), 0, 10.0)
    glTranslatef(0, 0, -5.0)
    generates_cubes(3)

    mouse_drag = False

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.__dict__['key'] == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.__dict__['button'] == pygame.BUTTON_LEFT:
                    mouse_drag = True
                elif event.__dict__['button'] == pygame.BUTTON_WHEELUP:
                    glTranslatef(0.1, 0, 0.1)
                elif event.__dict__['button'] == pygame.BUTTON_WHEELDOWN:
                    glTranslatef(-0.1, 0, -0.1)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.__dict__['button'] == pygame.BUTTON_LEFT:
                    mouse_drag = False

        if(mouse_drag):
            current_pos = pygame.mouse.get_pos()
            abs_diff1 = abs(current_pos[0] - mouse_pos[0])/4
            abs_diff2 = abs(current_pos[1] - mouse_pos[1])/4
            if mouse_pos[0] < current_pos[0]:
                glRotatef(0.5*abs_diff1, 0, 1, 0)
            else:
                glRotatef(0.5*abs_diff1, 0, -1, 0)

            if mouse_pos[1] < current_pos[1]:
                glRotatef(0.5*abs_diff2, 1, 0, 0)
            else:
                glRotatef(0.5*abs_diff2, -1, 0, 0)
            mouse_pos = current_pos

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(15)


if __name__ == "__main__":
    main()
