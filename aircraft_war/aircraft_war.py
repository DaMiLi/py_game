import pygame

from settings import Settings
from ship import Ship

import game_functions as gf

def run_game():
    pygame.init()
    aircraft_settings=Settings()
    screen=pygame.display.set_mode((aircraft_settings.screen_width,aircraft_settings.screen_height))
    ship=Ship(screen)
    pygame.display.set_caption("Aircraft War")
    
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(aircraft_settings,screen,ship)
        
run_game()