import image
from image import *
import pygame,test,userpage,playGame
from pygame.locals import *
from sys import exit
import player

pygame.init()
clock = pygame.time.Clock()

class Points():
    def __init__(self):
        self.Info=[]
        self.Info=player.getValue("data/recoder.txt")
        self.FPS = 60
        self.currentPoint = 2
        self.selectedPoint = 0
        self.main()

    def createDisplay(self):
        self.screen = pygame.display.set_mode((1440,900), 0, 32)
        pygame.display.set_caption("Tower Defense")
        self.background = pygame.image.load(background_file).convert()

        self.first_point = pygame.image.load(first_point_file).convert_alpha()
        self.second_point = pygame.image.load(second_point_unable_file).convert_alpha()
        self.third_point = pygame.image.load(third_point_unable_file).convert_alpha()

    def updateDisplay(self):

        if  int(self.Info[4]) >= 0:
            self.first_point = pygame.image.load(first_point_file).convert_alpha()

        if int(self.Info[4]) >= 1:
            self.second_point = pygame.image.load(second_point_file).convert_alpha()
        elif int(self.Info[4]) < 1:
            self.second_point = pygame.image.load(second_point_unable_file).convert_alpha()

        if int(self.Info[4]) >= 2:
            self.third_point = pygame.image.load(third_point_file).convert_alpha()
        elif int(self.Info[4]) < 2:
            self.third_point = pygame.image.load(third_point_unable_file).convert_alpha()

        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.first_point, (135,300))
        self.screen.blit(self.second_point, (570,300))
        self.screen.blit(self.third_point, (1005,300))

        
        pygame.display.flip()

    def detectWhichButton(self):
        x, y = pygame.mouse.get_pos()
        if (x>=135 and x<=(135+300)) and (y>=300 and y<=(300+300)):
            if int(self.Info[4]) >= 0:
                file = open("data/selected.txt", 'w', encoding = 'UTF-8')
                self.selectedPoint = "data\levels\level1.TD"
                file.write(self.selectedPoint)
                file.close()
                playGame.playGame()
            

        elif (x>=570 and x<=(570+300)) and (y>=300 and y<=(300+300)):
            if int(self.Info[4]) >= 1:
                file = open("data/selected.txt", 'w', encoding = 'UTF-8')
                self.selectedPoint = "data\levels\level2.TD"
                file.write(self.selectedPoint)
                file.close()
                playGame.playGame()
            

        elif (x>=1005 and x<=(1005+300)) and (y>=300 and y<=(300+300)):
            if int(self.Info[4]) >= 2:
                file = open("data/selected.txt", 'w', encoding = 'UTF-8')
                self.selectedPoint = "data\levels\level3.TD"
                file.write(self.selectedPoint)
                file.close()
                playGame.playGame()
           


    def main(self):

        self.createDisplay()
        while True:
            #mouse_left, mouse_mid, mouse_right = pygame.mouse.get_pressed()
            """Set FPS"""
            time_passed_sec = clock.tick(self.FPS)/1000

            self.updateDisplay()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == MOUSEBUTTONUP:
                    self.detectWhichButton()


                if event.type == KEYDOWN:

                    if event.key == K_t:
                        test.Draw()

                    if event.key == K_f:
                        self.screen = pygame.display.set_mode((1440,900), HWSURFACE | FULLSCREEN, 32)
                    if event.key == K_SPACE:
                        userpage.Userpage()
                    else:
                        self.screen = pygame.display.set_mode((1440,900), 0, 32)


if __name__ == '__main__':
    obj = Points()
