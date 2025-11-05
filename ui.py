import pygame
from constants import *

class UIManager:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(None, 24)

    def draw(self, screen, player):
        items = [
            ("SCORE", player.score),
            ("HEALTH", player.health),
            ("INVISIBILITY", f"{player.invisibility_timer:.1f}")
        ]
        for i, (name, value) in enumerate(items):
            y = UI_START_POS * (i + 1)
            text = self.font.render(f"{name}: {value}", True, (255, 255, 255))
            screen.blit(text, (UI_START_POS, y))