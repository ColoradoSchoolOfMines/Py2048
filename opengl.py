#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pySFML - Python bindings for SFML
# Copyright 2012-2013, Jonathan De Wachter <dewachter.jonathan@gmail.com>
#
# This software is released under the LGPLv3 license.
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

import sfml as sf

# create the main window
window = sf.RenderWindow(sf.VideoMode(800, 600), "pySFML - OpenGL"
        , sf.Style.DEFAULT, sf.ContextSettings(32))
window.vertical_synchronization = True

# load a font for drawing some text
font = sf.Font.from_file("resources/sansation.ttf")

# create a sprite for the background
background_texture = sf.Texture.from_file("resources/background.jpg")
background = sf.Sprite(background_texture)

# load an OpenGL texture.
# we could directly use a sf.Texture as an OpenGL texture (with its bind() member function),
# but here we want more control on it (generate mipmaps, ...) so we create a new one from an image
texture = 0
image = sf.Image.from_file("resources/texture.jpg")
glGenTextures(1, texture)
glBindTexture(GL_TEXTURE_2D, texture)
gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGBA, image.size.x, image.size.y, GL_RGBA, GL_UNSIGNED_BYTE, image.pixels.data)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)

# enable Z-buffer read and write
glEnable(GL_DEPTH_TEST)
glDepthMask(GL_TRUE)
glClearDepth(1)

# setup a perspective projection
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(90, 1, 1, 500)

# bind our texture
glEnable(GL_TEXTURE_2D)
glBindTexture(GL_TEXTURE_2D, texture)
glColor4f(1, 1, 1, 1)

# create a clock for measuring the time elapsed
clock = sf.Clock()

class Box:
    def __init__(self, value, x, y:
        self.value = value

        # Drawing related metrics
        self.x = x
        self.y = y
        self.sizex = 10
        self.sizey = 10
        self.sizez = 0

    # def translate(self, dx, dy):
    #     self.x += dx
    #     self.y += dy

    # Draw this box at a given location
    def draw(self, x, y):
        # apply some transformations
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(i*window.size.x/boardsize, j*window.size.y/boardsize, -100)

        glBegin(GL_QUADS)

        glTexCoord2f(0, 0)
        glVertex3f(-self.sizex, -self.sizey, -self.sizez)
        glTexCoord2f(0, 1)
        glVertex3f(-self.sizex,  self.sizey, -self.sizez)
        glTexCoord2f(1, 1)
        glVertex3f( self.sizex,  self.sizey, -self.sizez)
        glTexCoord2f(1, 0)
        glVertex3f( self.sizex, -self.sizey, -self.sizez)

        glTexCoord2f(0, 0)
        glVertex3f(-self.sizex, -self.sizey, self.sizez)
        glTexCoord2f(0, 1)
        glVertex3f(-self.sizex,  self.sizey, self.sizez)
        glTexCoord2f(1, 1)
        glVertex3f( self.sizex,  self.sizey, self.sizez)
        glTexCoord2f(1, 0)
        glVertex3f( self.sizex, -self.sizey, self.sizez)

        glTexCoord2f(0, 0)
        glVertex3f(-self.sizex, -self.sizey, -self.sizez)
        glTexCoord2f(0, 1)
        glVertex3f(-self.sizex,  self.sizey, -self.sizez)
        glTexCoord2f(1, 1)
        glVertex3f(-self.sizex,  self.sizey,  self.sizez)
        glTexCoord2f(1, 0)
        glVertex3f(-self.sizex, -self.sizey,  self.sizez)

        glTexCoord2f(0, 0)
        glVertex3f(self.sizex, -self.sizey, -self.sizez)
        glTexCoord2f(0, 1)
        glVertex3f(self.sizex,  self.sizey, -self.sizez)
        glTexCoord2f(1, 1)
        glVertex3f(self.sizex,  self.sizey,  self.sizez)
        glTexCoord2f(1, 0)
        glVertex3f(self.sizex, -self.sizey,  self.sizez)

        glTexCoord2f(0, 1)
        glVertex3f(-self.sizex, -self.sizey,  self.sizez)
        glTexCoord2f(0, 0)
        glVertex3f(-self.sizex, -self.sizey, -self.sizez)
        glTexCoord2f(1, 0)
        glVertex3f( self.sizex, -self.sizey, -self.sizez)
        glTexCoord2f(1, 1)
        glVertex3f( self.sizex, -self.sizey,  self.sizez)

        glTexCoord2f(0, 1)
        glVertex3f(-self.sizex, self.sizey,  self.sizez)
        glTexCoord2f(0, 0)
        glVertex3f(-self.sizex, self.sizey, -self.sizez)
        glTexCoord2f(1, 0)
        glVertex3f( self.sizex, self.sizey, -self.sizez)
        glTexCoord2f(1, 1)
        glVertex3f( self.sizex, self.sizey,  self.sizez)

        glEnd()


def boxSpawn():
    # Randomly choose a location for a box to spawn

# start game loop
while window.is_open:

        # process events
        for event in window.events:

                # close window : exit
                if event == sf.CloseEvent:
                        window.close()

                # escape key : exit
                if event == sf.KeyEvent and event.code == sf.Keyboard.ESCAPE:
                        window.close()

                # adjust the viewport when the window is resized
                if event == sf.ResizeEvent:
                        glViewport(0, 0, event.width, event.height)

        # draw the background
        window.push_GL_states()
        window.draw(background)
        window.pop_GL_states()


        # activate the window before using OpenGL commands.
        # this is useless here because we have only one window which is
        # always the active one, but don't forget it if you use multiple windows
        window.active = True

        # clear the depth buffer
        glClear(GL_DEPTH_BUFFER_BIT);

        # we get the position of the mouse cursor, so that we can move the box accordingly
        # x = sf.Mouse.get_position(window).x * 200. / window.size.x - 100.
        # y = -sf.Mouse.get_position(window).y * 200. / window.size.y + 100.

        # for box in boxes:
        #    box.draw()
        for box, i, j in boxIterate():
            # Draw the box that's in grid space i,j

        # draw some text on top of our OpenGL object
        window.push_GL_states()
        text = sf.Text("pySFML / OpenGL demo", font)
        text.color = sf.Color(255, 255, 255, 170)
        text.position = (230, 450)
        window.draw(text)
        window.pop_GL_states()

        # finally, display the rendered frame on screen
        window.display()

# don't forget to destroy our texture
glDeleteTextures(1, texture)
