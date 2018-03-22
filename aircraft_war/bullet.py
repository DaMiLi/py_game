import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ class to manage bullets fired by the shop."""
    def __init__(self,aircraft_settings,screen,ship):
        super().__init__()
        self.screen=screen
        
        self.rect=pygame.Rect(0,0,aircraft_settings.bullet_width,aircraft_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        
        self.y=float(self.rect.y)
        
        self.color=aircraft_settings.bullet_color
        self.speed_factor=aircraft_settings.bullet_speed_factor
    
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    
    
    
    
    
    