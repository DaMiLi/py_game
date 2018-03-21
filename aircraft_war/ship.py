import pygame

class Ship():
    def __init__(self,screen):
        self.screen=screen
    
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
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.bottom -= 1
        if self.moving_down:
            self.rect.bottom += 1    
            
            
            
            
            
            