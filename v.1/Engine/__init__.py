import pygame , sys , OpenGL , Engine
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import Engine.object
import Texture.json_manager as texture
import Engine.camera




pygame.init()
"""Enter object There       VVVV"""
my_objects = "Cube"
cmddown = False


class engine2:

    def main():
        
        pygame.init()
        display = (1840,1000)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

        glTranslatef(0.0,0.0,-5)
        
        while True:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            Engine.object.objects.start(my_objects)
            Engine.camera.camera2.camera_movement()
            # Engine.camera.camera2.auto_rotate(0.25,0,0.3,0)
            pygame.display.flip()
            pygame.time.wait(10)