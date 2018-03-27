import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard

import game_functions as gf

def run_game():
    pygame.init()
    aircraft_settings = Settings()
    screen = pygame.display.set_mode(
        (aircraft_settings.screen_width, aircraft_settings.screen_height))
    pygame.display.set_caption("Aircraft War")
    
    play_button = Button(aircraft_settings, screen, "play")
    
    stats = GameStats(aircraft_settings)
    sb = Scoreboard(aircraft_settings, screen, stats)
    
    
    ship = Ship(aircraft_settings, screen)
    bullets = Group()
    aliens = Group()
    
    gf.create_fleet(aircraft_settings, screen, ship, aliens)
    
    while True:
        gf.check_events(aircraft_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(aircraft_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(aircraft_settings, screen, stats, sb, ship, aliens, bullets)
            
        gf.update_screen(aircraft_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
run_game()