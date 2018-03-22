import pygame

class Ship():
    def __init__(self,aircraft_settings,screen):
        self.screen=screen
        self.aircraft_settings=aircraft_settings
    
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.scree_rect=screen.get_rect()
        
        self.rect.centerx=self.scree_rect.centerx
        self.rect.bottom=self.scree_rect.bottom
        
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        if self.moving_right:
            if self.rect.centerx<=self.aircraft_settings.screen_width-30:
                self.rect.centerx += self.aircraft_settings.ship_speed
        if self.moving_left:
            if self.rect.centerx>=30:
                self.rect.centerx -= self.aircraft_settings.ship_speed
        if self.moving_up:
            if self.rect.bottom>=50:
                self.rect.bottom -= self.aircraft_settings.ship_speed
        if self.moving_down:
            if self.rect.bottom<self.aircraft_settings.screen_height:
                self.rect.bottom += self.aircraft_settings.ship_speed
            
            
            
            
            
            