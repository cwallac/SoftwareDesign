# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 10:46:23 2014

@author: cwallace
"""

import pygame
from pygame.locals import *
import random
import math
import time

GameLost = 0
class DoodleJumpModel:
    def __init__(self):
        self.platforms = []
        for num in range(1,4):
            for plat in range(1,6):
            
                platform = Platform((0,135,0),random.randint(-75,75)+num*200,plat*120)
                self.platforms.append(platform)
        self.character = Jumper(100,100)
        
                
    def update(self):
        for plat in self.platforms:
            plat.update()
            if plat.y > 400:
                self.platforms.remove(plat)
            if self.character.y > 480:
                return 1
                
                
            self.character.jump()
        
    
    def newRow(self):
        for num in range(1,4):
            
                platform = Platform((0,135,0),random.randint(-75,75)+num*150,0)
                self.platforms.append(platform)
    
    def Collision(self):
        for base in self.platforms:
            if self.character.x in range(base.x-50,base.x+50):
                
                
                self.character.direction = -1
                
        

        
        
class Platform:
    def __init__(self,color,x,y):
        self.color = color
        self.x = x
        self.y = y
        
    def update(self):
        self.y += .5
        
class Jumper:
    def __init__(self,x,y):
        self.color = (133,133,133)
        self.x = x
        self.y = y
        self.isOnPlatform = 0 
        self.isJumping = 0
        self.vx = 0
        self.vy = .7

        self.direction = 1
    
    def jump(self):

        if self.isOnPlatform == 1:
            self.vy = .5
        
        
        
        
        if self.x > 640:
            self.x = 20
            
            
        if self.x < 0:
            self.x = 620
         
        self.x += self.vx
        self.y += self.vy
        
class PyGameMouseController:
    def __init__(self,model):
        self.model = model
    
    def handle_mouse_event(self,event):
        if event.type == MOUSEMOTION:
            self.model.character.x = event.pos[0] - 12.5
        
class PyGameKeyboardController:
    """ Handles keyboard input for brick breaker """
    def __init__(self,model):
        self.model = model
    
    def handle_keyboard_event(self,event):
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            if self.model.character.vx >= -3:
                self.model.character.vx += -1.0
                
        if event.key == pygame.K_UP:
            self.model.character.isJumping = 1
            
        if event.key == pygame.K_SPACE:
            print "GAME START"
            return True
            
                
        if event.key == pygame.K_RIGHT:
            if self.model.character.vx <= 3:
                self.model.character.vx += 1.0        

class PyGameWindowView:
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        for brick in self.model.platforms:
    
            pygame.draw.rect(self.screen, pygame.Color(235,0,0),pygame.Rect(brick.x,brick.y,100,25))
            pygame.draw.rect(self.screen, pygame.Color(133,133,133),pygame.Rect(self.model.character.x,self.model.character.y,25,25))     
        pygame.display.update()
        
    def Loser(self):
        
        img=pygame.image.load('Game_Over.jpg')
        pygame.display.flip()
        screen.blit(img,(0,0))

        

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = DoodleJumpModel()
    view = PyGameWindowView(model,screen)
    

    controller = PyGameKeyboardController(model)

    running = True
    count = 0
    Started = 0
    while running:
        
        count += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                controller.handle_keyboard_event(event)
                
                if controller.handle_keyboard_event(event) == True:
                    Started = 1
                    print 'GAME SHOULD START...'
                    
                    
            
    
         
    
            if event.type == QUIT:
                running = False
                break
                
            #if event.type == MOUSEMOTION:
             #   controller.handle_mouse_event(event)
    
        if Started == 0:
            time.sleep(.001)
        else:
            if count % 250 == 0:
                model.newRow()
            model.Collision()
            model.update()
                
            if model.update() == 1:
                view.Loser()
            else:
                view.draw()
            time.sleep(.1)
        

    pygame.quit()