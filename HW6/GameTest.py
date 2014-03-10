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
    '''Model for game Block Jump'''
    
    def __init__(self):
        self.platforms = []
        for num in range(1,4):
            for plat in range(1,6):
            
                platform = Platform((0,135,0),random.randint(-75,75)+num*200,plat*120,80,10)
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
            
                platform = Platform((0,135,0),random.randint(-75,75)+num*150,0,80,10)
                self.platforms.append(platform)
    
    def Collision(self):
        for base in self.platforms:
            if not ((self.character.x+20<base.x) or (self.character.x>base.x+base.length)): 
                if not ((self.character.y+20 < (base.y)) or (self.character.y > base.y+base.width)):
                     
                    self.character.isOnPlatform = 1
                    self.character.JumpingTimer = 220
                
        

        
        
class Platform:
    ''' PLATFORMS to jump on'''
    
    def __init__(self,color,x,y,length,width):
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        
    def update(self):
        self.y += .7
        
class Jumper:
    '''BRICK THAT HUMAN CONTROLS'''
    def __init__(self,x,y):
        self.color = (133,133,133)
        self.x = x
        self.y = y
        self.isOnPlatform = 0 
        self.JumpingTimer = 0
        self.vx = 0
        self.vy = .7

        self.direction = 1
    
    def jump(self):
        self.JumpingTimer += -1 
        if self.JumpingTimer > 0:
            self.vy = -.7
        else:
            self.vy = .7
        
        
        
        
        if self.x > 640:
            self.x = 20
            
            
        if self.x < 0:
            self.x = 620
         
        self.x += self.vx
        
        self.y += self.vy
        

        
class PyGameKeyboardController:
    """ Handles keyboard input for Block Jump """
    def __init__(self,model):
        self.model = model
    
    def handle_keyboard_event(self,event):
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            if self.model.character.vx >= -1.5:
                self.model.character.vx += -.1
                
        if event.key == pygame.K_UP:
            self.model.character.isJumping = 1
            
        if event.key == pygame.K_SPACE:
            print "GAME START"
            return True
            
                
        if event.key == pygame.K_RIGHT:
            if self.model.character.vx <= 1.5:
                self.model.character.vx += .1       

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
        ''' SCreen displayed after loss'''
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
            count += 1
            
            if count == 50:
              model.newRow()  
            elif count % 140 == 0:
               model.newRow() 
            model.Collision()
            model.update()
                
            if model.update() == 1:
                view.Loser()
                
                
            else:
                view.draw()
            time.sleep(.05)
        

    pygame.quit()

