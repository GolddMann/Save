import pygame
from math import cos, sin, acos, tan, sqrt, acos

rotate_speed = 0.1
size = width, height = 800, 600
origin = (width/2, height/2)

dots = [[[-100, 100, 0], [100, 100, 0]], [
    [100, 100, 0], [100, -100, 0]], [[-100, -100, 0], [100, -100, 0]], [[-100, -100, 0], [-100, 100, 0]],
    [[-100, 100, 200], [100, 100, 200]], [[100, 100, 200],
                                          [100, -100, 200]], [[-100, -100, 200], [100, -100, 200]],
    [[-100, -100, 200], [-100, 100, 200]], [[-100, 100, 0], [-100, 100, 200]], [[100, 100, 0], [100, 100, 200]], [[-100, -100, 0], [-100, -100, 200]], [[100, -100, 0], [100, -100, 200]]]

distance = 400
viewer_plane = [0, 0, 0]
p_a1 = 0
p_a2 = 0
view_angle = 120
plane_d = 40


BG_COLOR = (0, 0, 0)
CUBE_COLOR = (255, 255, 255)


def rotate():
    for dot in dots:
        for i in range(2):
            x = dot[i][0]
            y = dot[i][1]

            radians = rotate_speed*acos(-1)/180.0

            dot[i][0] = x*cos(radians) - \
                y*sin(radians)
            dot[i][1] = x*sin(radians) + \
                y*cos(radians)


def draw_cube(screen):
    proj_plane = [distance*cos(p_a1)*cos(p_a2),
                  distance*cos(p_a1)*sin(p_a2), distance*sin(p_a1)]
    viewer_point = [proj_plane[0]+plane_d,
                    proj_plane[1]+plane_d, proj_plane[2] + plane_d]
    view_angle_radians = view_angle*acos(-1)/180.
    p_size = plane_d*tan(view_angle_radians)

    dots_2d = []

    for i in range(len(dots)):
        line = []
        for j in range(2):
            dot = []
            x = dots[i][j][0]
            y = dots[i][j][1]
            z = dots[i][j][2]
            w_x = viewer_point[0]
            w_y = viewer_point[1]
            w_z = viewer_point[2]
            v1 = [w_x - x, w_y - y, w_z - z]
            v2 = [w_x - proj_plane[0], w_y -
                  proj_plane[1], w_z - proj_plane[2]]
            angle1 = (v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])/(sqrt(v1[0]*v1[0] + v1[1]
                                                                     * v1[1] + v1[2]*v1[2])*sqrt(v2[0]*v2[0] + v2[1]*v2[1] + v2[2]*v2[2]))
            v3 = [proj_plane[0], proj_plane[1], proj_plane[2] - 1]
            v4 = [w_x - x, w_y - y, w_z - z]
            angle2 = (v3[0]*v4[0] + v3[1]*v4[1] + v3[2]*v4[2])/(sqrt(v3[0]*v3[0] + v3[1]
                                                                     * v3[1] + v3[2]*v3[2])*sqrt(v4[0]*v4[0] + v4[1]*v4[1] + v4[2]*v4[2]))
            new_x = plane_d*tan(acos(angle1))*angle2
            new_y = plane_d*tan(acos(angle1))*sin(acos(angle2))
            dot.append(new_x)
            dot.append(new_y)
            line.append(dot)
        dots_2d.append(line)

    for line in dots_2d:
        pygame.draw.line(
            screen, CUBE_COLOR, (line[0][0] + 300, line[0][1] + 200), (line[1][0] + 300, line[1][1] + 200), 2)


def main():
    global distance, p_a1, p_a2
    pygame.init()
    screen = pygame.display.set_mode(size)
    mouse_draging = False

    mouse_coords = pygame.mouse.get_pos()

    while True:
        for event in pygame.event.get():

            if(event.type == 256):
                pygame.quit()
                exit(0)
            elif(event.type == 1025):
                if(event.__dict__['button'] == 5):
                    distance += 10
                elif(event.__dict__['button'] == 4):
                    distance -= 10
                elif(event.__dict__['button'] == 1):
                    mouse_draging = True
            elif(event.type == 1026):
                if(event.__dict__['button'] == 1):
                    mouse_draging = False

            elif(event.type == 1024):
                if(mouse_draging):
                    if(mouse_coords[0] - event.__dict__['pos'][0] > 0):
                        p_a1 -= 0.01
                    else:
                        p_a1 += 0.01

                    if(mouse_coords[1] - event.__dict__['pos'][1] > 0):
                        p_a2 -= 0.01
                    else:
                        p_a2 += 0.01
                mouse_coords = event.__dict__['pos']

        screen.fill(BG_COLOR)
        draw_cube(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
