from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import Texture.json_manager as texture
import Engine.camera
from math import sin , cos , pi


cmddown = False


class Object3D:
    def __init__(self,vertices, edges, surfaces, colors, nesbat):
        self.vertices = vertices
        self.edges = edges
        self.color = colors
        self.surface = surfaces
        self.nesbat = nesbat


class objects:
    def load(name):

        """place your name file and give return the vertices and edges"""

        texture.objects.open_file(name)
        vertices, edges, surfaces, color, nesbat = texture.objects.varible(True,True,True,True,True)


        return vertices, edges, surfaces, color, nesbat
    


    #BUG : Index out of range in obj varible
    def load_surfaces(vertices, surfaces, color, nesbat):
        
        glColor3fv(color)
        glBegin(GL_QUADS)
        for surface in surfaces:
            for vertex in surface:
                obj =(vertices[vertex][0] / nesbat, vertices[vertex][1] / nesbat, vertices[vertex][2] / nesbat)
                glVertex3fv(obj)
                
        glEnd()
        


    def load_lines(vertices, edges, color, nesbat):
        glColor3fv(color)
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                obj =(vertices[vertex][0] / nesbat, vertices[vertex][1] / nesbat, vertices[vertex][2] / nesbat)
                glVertex3fv(obj)
                
        glEnd()
        

    def start(list_name):

        vertices, edges, surfaces, colors, nesbat = objects.load(list_name)
        my_object = Object3D(vertices, edges, surfaces, colors, nesbat)
            
        if edges != None :
            objects.load_lines(my_object.vertices, my_object.edges, my_object.color, my_object.nesbat)

        if surfaces != None :
            objects.load_surfaces(my_object.vertices, my_object.surface, my_object.color, my_object.nesbat)

        





