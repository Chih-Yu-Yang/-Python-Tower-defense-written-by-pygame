import image
from image import *
import pygame
import inputpage
import userpage
from pygame.locals import *
from sys import exit
import os


class Homepage:
    fullscreen=0
    def initialstart(self,backgroundpicture,x,y):
        pygame.init()
        pygame.mixer.init()
        screen=pygame.display.set_mode((x,y),0,32)
        background = pygame.image.load(backgroundpicture).convert()
        screen.blit(background, (0,0))
        pygame.mixer.music.load( "music.mp3 " )
        pygame.mixer.music.play(-1)
        return (screen)
    def setpicture(self,screen,picturename,x,y):
        picture=pygame.image.load(picturename)
        picture=picture.convert()
        screen.blit(picture,(x,y))
    def show(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
                    elif event.key == K_f:
                        screen = pygame.display.set_mode((800, 600), FULLSCREEN, 32)
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            if pygame.mouse.get_pressed()[0]:
                if ((pygame.mouse.get_pos()[0])>560 and (pygame.mouse.get_pos()[0])<860 and (pygame.mouse.get_pos()[1])>600 and (pygame.mouse.get_pos()[1])<683):
                    inputpage.Inputpage()
                elif ((pygame.mouse.get_pos()[0])>560 and (pygame.mouse.get_pos()[0])<860 and (pygame.mouse.get_pos()[1])>700 and (pygame.mouse.get_pos()[1])<783):
                    if(os.path.exists("data/recoder.txt")):
                        userpage.Userpage()
                    else:
                        inputpage.Inputpage()
                elif ((pygame.mouse.get_pos()[0])>560 and (pygame.mouse.get_pos()[0])<860 and (pygame.mouse.get_pos()[1])>800 and (pygame.mouse.get_pos()[1])<883):
                    pygame.quit()
                    exit()
            pygame.display.update()
    def __init__(self):
        screen=self.initialstart(background_file,1440,900)
        self.setpicture(screen,newgame,560,600)
        self.setpicture(screen,continuep,560,700)
        self.setpicture(screen,quitgame,560,800)
        self.show()

if __name__ == '__main__':
    start = Homepage()
