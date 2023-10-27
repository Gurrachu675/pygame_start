# initialize
import pygame

pygame.init() 

#game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ECS snake game")
clock = pygame.time.Clock()
