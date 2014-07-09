import image
from image import *
import random
import pygame
from pygame.locals import *
from sys import exit
import rider
from rider import *
import solider
from solider import *
import archer
from archer import *
import player
import lv_Table
import userpage
fscrn = False

pygame.init()
clock = pygame.time.Clock()
class playGame:
    def __init__(self):

        self.file = open("data\selected.txt", 'r', encoding = 'UTF-8')
        self.lvlT=self.file.readline()
        self.file.close()
        self.lvl=[]
        self.lvl=player.getValue(self.lvlT)
        self.money = 2000
        self.sodier_cost = 100
        self.archer_cost = 500
        self.rider_cost = 1000
        self.FPS = 60
        self.check=0
        self.type=0
        self.counter=0
        self.Info=[]
        self.Info=player.getValue("data/recoder.txt")
        self.TotalHPA=int(1000*(1.2**float(self.Info[1])))
        self.NowHPA=self.TotalHPA
        self.s=[]
        self.e=[]
        self.alx=[100]
        self.aly=[]
        self.emx=[1260]
        self.emy=[]
        self.lvup=0
        self.TotalHPE=int(self.lvl[12])
        self.NowHPE=int(self.lvl[12])
        self.main()

    def createDisplay(self):
        self.screen = pygame.display.set_mode((1440,900), 0, 32)
        pygame.display.set_caption("Tower Defense")
        self.background = pygame.image.load(background_file).convert()
        self.sodier = pygame.image.load(sodier_able_file).convert_alpha()
        self.archer = pygame.image.load(archer_able_file).convert_alpha()
        self.rider = pygame.image.load(rider_able_file).convert_alpha()     
        self.ally_tower = pygame.image.load(ally_tower_file).convert_alpha()
        self.enemy_tower = pygame.image.load(enemy_tower_file).convert_alpha()
        self.sA=pygame.image.load(soliderA).convert_alpha()
        self.rA=pygame.image.load(riderA).convert_alpha()
        self.aA=pygame.image.load(archerA).convert_alpha()
        self.sE=pygame.image.load(soliderE).convert_alpha()
        self.rE=pygame.image.load(riderE).convert_alpha()
        self.aE=pygame.image.load(archerE).convert_alpha()
        self.defeat=pygame.image.load(defeat_file).convert_alpha()
        self.victory=pygame.image.load(victory_file).convert_alpha()
    ##刷新畫面用
    def updateDisplay(self):
        if self.money >= self.sodier_cost and self.Info[6]=="1":
            self.sodier = pygame.image.load(sodier_able_file).convert_alpha()
        elif self.money <= self.sodier_cost or self.Info[6]=="0":
            self.sodier = pygame.image.load(sodier_unable_file).convert_alpha()

        if self.money >= self.archer_cost and self.Info[9]=="1":
            self.archer = pygame.image.load(archer_able_file).convert_alpha()
        elif self.money <= self.archer_cost or self.Info[9]=="0":
            self.archer = pygame.image.load(archer_unable_file).convert_alpha()

        if self.money >= self.rider_cost and self.Info[12]=="1":
            self.rider = pygame.image.load(rider_able_file).convert_alpha()
        elif self.money <= self.rider_cost or self.Info[12]=="0":
            self.rider = pygame.image.load(rider_unable_file).convert_alpha()
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.sodier, (100,775))
        self.screen.blit(self.archer, (250,775))
        self.screen.blit(self.rider, (400,775))
        self.screen.blit(self.ally_tower, (0,455))
        self.screen.blit(self.enemy_tower, (1240,455))
        
    
        if(self.lvl[0]=="1" and self.counter%3==0):
            if(random.randint(0,241)%int(self.lvl[1])==0):
                self.e.append(solider(int(self.lvl[2])))
                self.e[len(self.e)-1].setValue()
                self.e[len(self.e)-1].x=1300
                self.emx.append(self.e[len(self.e)-1].x)
                self.emy.append(self.e[len(self.e)-1].y)
        if(self.lvl[3]=="1" and self.counter%3==1):
            if(random.randint(0,241)%int(self.lvl[4])==0):
                self.e.append(archer(int(self.lvl[5])))
                self.e[len(self.e)-1].setValue()
                self.e[len(self.e)-1].x=1300
                self.emx.append(self.e[len(self.e)-1].x)
                self.emy.append(self.e[len(self.e)-1].y)
        if(self.lvl[6]=="1" and self.counter%3==2):
            if(random.randint(0,241)%int(self.lvl[7])==0):
                self.e.append(rider(int(self.lvl[8])))
                self.e[len(self.e)-1].setValue()
                self.e[len(self.e)-1].x=1300
                self.emx.append(self.e[len(self.e)-1].x)
                self.emy.append(self.e[len(self.e)-1].y)
        
        if(len(self.s)>0):
            for i in range(0,len(self.s)):
                if(self.s[i].islive==1):
                    tmp=[]
                    tmp=self.s[i].attack_b(self.emx,0)
                    if(tmp[0]):
                        self.alx[i+1]=self.s[i].move(self.alx[i+1],0)
                        self.s[i].x=self.alx[i+1]
                    else:
                        if(tmp[1]==0):
                            self.NowHPE-=self.s[i].getAttack()
                        else:
                            self.e[tmp[1]-1].attacked(self.s[i].getAttack())
                            if(self.e[tmp[1]-1].islive==-1):
                                if(self.e[tmp[1]-1].type==1):
                                    self.money+=50
                                elif(self.e[tmp[1]-1].type==2):
                                    self.money+=80
                                elif(self.e[tmp[1]-1].type==3):
                                    self.money+=200
                    if(self.s[i].type==1):
                        self.screen.blit(self.sA, (self.alx[i+1],self.aly[i]))
                    elif(self.s[i].type==2):
                        self.screen.blit(self.rA, (self.alx[i+1],self.aly[i]))
                    elif(self.s[i].type==3):
                        self.screen.blit(self.aA, (self.alx[i+1],self.aly[i]))
                elif(self.s[i].islive==-1):
                    self.alx[i+1]=0;
                    self.aly[i]=self.s[i].move(self.aly[i],2)
                    self.s[i].y=self.aly[i]
                    if(self.s[i].type==1):
                        self.screen.blit(self.sA, (self.s[i].x,self.aly[i]))
                    elif(self.s[i].type==2):
                        self.screen.blit(self.rA, (self.s[i].x,self.aly[i]))
                    elif(self.s[i].type==3):
                        self.screen.blit(self.aA, (self.s[i].x,self.aly[i]))
        if(len(self.e)>0):
            for i in range(0,len(self.e)):
                if(self.e[i].islive==1):
                    tmp=[]
                    tmp=self.e[i].attack_b(self.alx,1)
                    if(tmp[0]):
                        self.emx[i+1]=self.e[i].move(self.emx[i+1],1)
                        self.e[i].x=self.emx[i+1]
                    else:
                        if(tmp[1]==0):
                            self.NowHPA-=self.e[i].getAttack()
                        else:
                            self.s[tmp[1]-1].attacked(self.e[i].getAttack())
                    if(self.e[i].type==1):
                        self.screen.blit(self.sE, (self.emx[i+1],self.emy[i]))
                    elif(self.e[i].type==2):
                        self.screen.blit(self.rE, (self.emx[i+1],self.emy[i]))
                    elif(self.e[i].type==3):
                        self.screen.blit(self.aE, (self.emx[i+1],self.emy[i]))
                elif(self.e[i].islive==-1):
                    self.emx[i+1]=1440
                    self.emy[i]=self.e[i].move(self.emy[i],2)
                    self.e[i].y=self.emy[i]
                    if(self.e[i].type==1):
                        self.screen.blit(self.sE, (self.e[i].x,self.emy[i]))
                    elif(self.e[i].type==2):
                        self.screen.blit(self.rE, (self.e[i].x,self.emy[i]))
                    elif(self.e[i].type==3):
                        self.screen.blit(self.aE, (self.e[i].x,self.emy[i]))

        
        self.counter+=1
        if(self.counter==15):
            self.money+=1
            self.counter=0
            

            
        self.myfont = pygame.font.SysFont("monospace", 24)
        self.textImg = self.myfont.render("HP:"+str(self.NowHPA)+"/"+str(self.TotalHPA),1,(255,255,255))
        self.screen.blit(self.textImg,(50,450))
        self.textImg = self.myfont.render("HP:"+str(self.NowHPE)+"/"+str(self.TotalHPE),1,(255,255,255))
        self.screen.blit(self.textImg,(1250,450))
        self.myfont = pygame.font.SysFont("monospace", 18)
        self.textImg = self.myfont.render(self.Info[0],1,(255,255,255))
        self.screen.blit(self.textImg,(0,0))
        self.textImg = self.myfont.render("LV:"+self.Info[1],1,(255,255,255))
        self.screen.blit(self.textImg,(100,0))
        self.textImg = self.myfont.render("$:"+str(self.money),1,(255,255,255))
        self.screen.blit(self.textImg,(200,0))

        if(self.NowHPA<=0 and self.type!=2):
            self.type=1
            self.screen.blit(self.defeat, (0,0))
            if(self.check==0):
                self.result1="Defeat~ get "+str(int(int(self.lvl[9])/2))+" exp => "+self.Info[3]+"->"+str(int(int(self.Info[3])+int(self.lvl[9])/2))+" money => "+self.Info[2]+"->"+str(int(int(self.Info[2])+int(self.lvl[10])/2))
                self.result2="please press space to continue";
                self.Info[2]=str(int(self.Info[2])+int(int(self.lvl[10])/2))
                self.Info[3]=str(int(self.Info[3])+int(int(self.lvl[9])/2))
                if(int(self.Info[3])>=2**int(self.Info[1])):
                    self.Info[1]=str(int(self.Info[1])+1)
                    self.lvup=1
                player.setValue(self.Info)
            
            self.check=1
            if(self.lvup==1):
                self.myfont = pygame.font.SysFont("monospace", 60)
                self.textImg = self.myfont.render("Level Up "+str(int(self.Info[1])-1)+"->"+self.Info[1],1,(0,0,0))
                self.screen.blit(self.textImg,(200,200))
            
            self.myfont = pygame.font.SysFont("monospace", 40)
            self.textImg = self.myfont.render(self.result1,1,(0,0,0))
            self.screen.blit(self.textImg,(120,300))
            self.textImg = self.myfont.render(self.result2,1,(0,0,0))
            self.screen.blit(self.textImg,(120,350))
        elif(self.NowHPE<=0 and self.type!=1):
            self.type=2
            self.screen.blit(self.victory, (0,0))
            if(self.check==0):
                self.result1="Victory!!! get "+self.lvl[9]+" exp => "+self.Info[3]+"->"+str(int(self.Info[3])+int(self.lvl[9]))+" money => "+self.Info[2]+"->"+str(int(self.Info[2])+int(self.lvl[10]))
                self.result2="please press space to continue"
                self.Info[2]=str(int(self.Info[2])+int(self.lvl[10]))
                self.Info[3]=str(int(self.Info[3])+int(self.lvl[9]))
                if(int(self.lvl[11])>int(self.Info[4])):
                    self.Info[4]=str(int(self.Info[4])+1)
                if(int(self.Info[3])>=2**int(self.Info[1])):
                    self.Info[1]=str(int(self.Info[1])+1)
                    self.lvup=1
                player.setValue(self.Info)

            if(self.lvup==1):
                self.myfont = pygame.font.SysFont("monospace", 60)
                self.textImg = self.myfont.render("Level Up "+str(int(self.Info[1])-1)+"->"+self.Info[1],1,(0,0,0))
                self.screen.blit(self.textImg,(200,200))
                
            self.check=1
            self.myfont = pygame.font.SysFont("monospace", 40)
            self.textImg = self.myfont.render(self.result1,1,(0,0,0))
            self.screen.blit(self.textImg,(60,300))
            self.textImg = self.myfont.render(self.result2,1,(0,0,0))
            self.screen.blit(self.textImg,(60,350))

        
        #self.screen.fill((255,255,255))
        pygame.display.flip()
    """偵測按鍵"""
    def detectWhichButton(self):
        x, y = pygame.mouse.get_pos()
        if (x>=100 and x<=(100+111)) and (y>=775 and y<=(775+106)):
            if self.money >= self.sodier_cost and self.Info[6]=="1":
                
                
                self.s.append(solider(int(self.Info[7])))
                self.s[len(self.s)-1].setValue()
                self.alx.append(self.s[len(self.s)-1].x)
                self.aly.append(self.s[len(self.s)-1].y)
                self.money-=100
        elif (x>=250 and x<=(250+111)) and (y>=775 and y<=(775+106)):
            if self.money >= self.archer_cost and self.Info[9]=="1":
                self.s.append(archer(int(self.Info[10])))
                self.s[len(self.s)-1].setValue()
                self.alx.append(self.s[len(self.s)-1].x)
                self.aly.append(self.s[len(self.s)-1].y)
                self.money-=500
        elif (x>=400 and x<=(400+111)) and (y>=775 and y<=(775+106)):
            if self.money >= self.rider_cost and self.Info[12]=="1":
                self.s.append(rider(int(self.Info[13])))
                self.s[len(self.s)-1].setValue()
                self.alx.append(self.s[len(self.s)-1].x)
                self.aly.append(self.s[len(self.s)-1].y)
                self.money-=1000
    
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

                    if event.key == K_f:
                        self.screen = pygame.display.set_mode((1440,900), HWSURFACE | FULLSCREEN, 32)                
                    elif event.key== K_SPACE and self.type!=0:
                        userpage.Userpage()
                    else:
                         self.screen = pygame.display.set_mode((1440,900), 0, 32)
                    
                
if __name__ == '__main__':
    obj = playGame()






