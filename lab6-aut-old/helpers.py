import pygame 

class Geometry(object):

    @classmethod
    def get_direction_from_angle(cls, angle, length):
        """ Return x,y direction vector from angle and length"""
        rad_angle = math.radians(angle)
        x = length * math.cos(rad_angle)
        y = length * math.sin(rad_angle)
        return x,y

    @classmethod
    def get_angle_from_line(cls, x1, y1, x2, y2):
        """ Return angle in degrees from two points: 
            
            Params: 
            x1, y1 coordinates for point 1
            x2, y2 coordinates for point 2
        """
        dirx = x2 - x1
        diry = y2 - y1
        rad_angle = math.atan2(diry, dirx)
        deg_angle = rad_angle * 180/math.pi
        return deg_angle % 360

 

def center(size, fig):
    figw = fig.get_rect()[2]
    figh = fig.get_rect()[3]
    w = size[0]
    h = size[1]
    return (w/2 - figw/2, h/2 - figh/2)

def middle_x(size, fig, y):
    figw = fig.get_rect()[2]
    figh = fig.get_rect()[3]
    w = size[0]
    return (w/2 - figw/2, y - figh/2)

def load_fig(name, size):
    fig = pygame.image.load(name)
    fig = pygame.transform.scale(fig, size)
    return fig

def render_text(text, size, font="Arial", color=(255,255,255)):
    font = pygame.font.SysFont(font, size)
    return font.render(text, True, color)

