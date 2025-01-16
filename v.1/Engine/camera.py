import pygame , sys , OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class camera2:

    def camera_movement():
            # get keys
            keypress = pygame.key.get_pressed()

            if keypress[pygame.K_UP]:
                glRotate(0.25,0.3,0.0,0.0)

            if keypress[pygame.K_DOWN]:
                glRotate(0.25,-0.3,0.0,0.0)
            
            if keypress[pygame.K_LEFT]:
                glRotate(0.25,0.0,-0.3,0.0)
            
            if keypress[pygame.K_RIGHT]:
                glRotate(0.25,0.0,0.3,0.0)
            
            if keypress[pygame.K_e]:
                glRotate(0.25,0.0,0.0,0.3)
            
            if keypress[pygame.K_q]:
                glRotate(0.25,0.0,0.0,-0.3)
            

    # def auto_rotate(angle,x,y,z):
    #     glRotate(angle,x,y,z)
    
    # COMPLATE : Complate the cam
    # TEST : Test the camera
    # gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)