import image
from image import *
import pygame
from pygame.locals import *
from sys import exit
import userpage
import player
class Inputpage:
    def __init__(self):
        pygame.init()
        screen=pygame.display.set_mode((1440,900),0,32)
        background = pygame.image.load(inputpage).convert()
        screen.blit(background, (0,0))
        name = ""
        font = pygame.font.Font(None, 150)
        while True:
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    screen=pygame.display.set_mode((1440,900),0,32)
                    background = pygame.image.load(inputpage).convert()
                    screen.blit(background, (0,0))
                    if evt.unicode.isalpha():
                        name += evt.unicode
                    elif evt.key == K_BACKSPACE:
                        name = name[:-1]
                    elif evt.key == K_RETURN:

                        
                        player.setInitial(name)
                        userpage.Userpage()
                        #userpage.initial()
                elif evt.type == pygame.QUIT:
                        pygame.quit()
                        exit()
            block = font.render(name, True, (0, 0, 0))
            rect = block.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(block, rect)
            pygame.display.update()

if __name__ == '__main__':
    start = Inputpage()
