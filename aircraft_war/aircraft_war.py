import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from button import Button
from game_stats import GameStats

import game_functions as gf

def run_game():
    pygame.init()
    aircraft_settings = Settings()
    stats = GameStats(aircraft_settings)
    screen = pygame.display.set_mode((aircraft_settings.screen_width, aircraft_settings.screen_height))
    ship=Ship(aircraft_settings, screen)
    bullets = Group()
    pygame.display.set_caption("Aircraft War")
    
    play_button = Button(aircraft_settings, screen, "Play")
    
    while True:
        gf.check_events(aircraft_settings, screen,ship, bullets, play_button, stats)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets)
        gf.update_screen(aircraft_settings, screen, ship, bullets, play_button)
        
run_game()