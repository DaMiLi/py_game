import sys
import pygame

from bullet import Bullet

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(aircraft_settings, screen, ship, bullets, play_button, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(aircraft_settings, screen, event, ship, bullets, mouse_x, mouse_y, play_button, stats)
        
def check_play_button(aircraft_settings, screen, event, ship, bullets, mouse_x, mouse_y, play_button, stats):
    pass
            
def update_screen(aircraft_settings, screen, ship, bullets, play_button):
    screen.fill(aircraft_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
    
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

def fire_bullet(aircraft_settings,screen,ship,bullets):
    if len(bullets) < aircraft_settings.bullets_allowed:
        new_bullet = Bullet(aircraft_settings,screen,ship)
        bullets.add(new_bullet)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            