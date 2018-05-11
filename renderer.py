import environment as env
import pygame

WHITE = (255,255,255)
# Width of line
LINE_WIDTH = 3
POINT_RAD = 5

class Renderer():
    def __init__(self, width, height, title):
        pygame.init()
        self.disp_width = width
        self.disp_height = height

        self.screen = pygame.display.set_mode((self.disp_width, self.disp_height))
        self.screen.fill(WHITE)
        pygame.display.set_caption('Maze Simulator')

    def render_walls(self, walls):
        for wall in walls:
            color = wall.color
            ax = wall.ax
            ay = wall.ay
            bx = wall.bx
            by = wall.by
            pygame.draw.line(self.screen, color, [ax, ay], [bx,by], LINE_WIDTH)

    def render_robot(self, robot):
        x = int(robot.location[0])
        y = int(robot.location[1])
        radius = robot.default_robot_size
        pygame.draw.circle(self.screen, (0,0,0), [x, y], int(radius), LINE_WIDTH)

    def render_goal(self, goal):
        x = int(goal.x)
        y = int(goal.y)
        pygame.draw.circle(self.screen, (0,100,0), [x, y], POINT_RAD, LINE_WIDTH)

    def render_pois(self, pois):
        for poi in pois:
            x = int(poi.x)
            y = int(poi.y)
            pygame.draw.circle(self.screen, (0,0,100), [x, y], POINT_RAD, LINE_WIDTH)

    def render_aoi(self):
        x = 160
        y = 114
        pygame.draw.rect(self.screen, (255,0,0), [x, y, 263, 299], LINE_WIDTH)

    def render(self, env):
        self.screen.fill(WHITE)
        self.render_walls(env.walls)
        self.render_pois(env.pois)
        self.render_goal(env.goal)
        self.render_aoi()
        self.render_robot(env.robot)
        pygame.display.update() 