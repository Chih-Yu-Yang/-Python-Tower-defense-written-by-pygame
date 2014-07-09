import userpage,player,lv_Table
import pygame
from pygame.locals import *
from sys import exit
#商店頁面，點擊按鈕後，可查看print的資訊(強化值)

class shopPage:

    def __init__(self):
        
        '''需要從外部取得的資訊'''

        self.Info=[]
        self.Info=player.getValue("data/recoder.txt")
        
        #玩家剩餘金額
        
        self.userMoney = int(self.Info[2])

        #士兵是否被購買
        
        if(self.Info[6]=="0"):
            self.haveSodier = False
            self.SodierValue = 0
        else:
            self.haveSodier = True
            self.SodierValue = int(self.Info[7])

        if(self.Info[9]=="0"):
            self.haveArcher = False
            self.ArcherValue = 0
        else:
            self.haveArcher = True
            self.ArcherValue = int(self.Info[10])

        if(self.Info[12]=="0"):
            self.haveRider  = False
            self.RiderValue = 0
        else:
            self.haveRider  = True
            self.RiderValue = int(self.Info[13])
      
        '''內部取得的資訊'''

        #其餘參數

        self.screensize=(1400,900)
        self.background_file ='img/background_shop.jpg'
        self.sodier_able_file = 'img/sodier_able.png'
        self.archer_able_file = 'img/archer_able.png'
        self.rider_able_file = 'img/rider_able.png'
        self.sodier_unable_file = 'img/sodier_unable.png'
        self.archer_unable_file = 'img/archer_unable.png'
        self.rider_unable_file = 'img/rider_unable.png'
        self.buy_file='img/buy.png'
        self.strong_file='img/strong.png'

        pygame.init()
        pygame.display.set_caption("shop")
        self.screen = pygame.display.set_mode(self.screensize,0,32) 

        #如果需要修改圖片，只需要修改清單，就可以自動化完成所有修改
        
        '''士兵資訊          0名稱     1士兵是否買了      2士兵強化值        3士兵解鎖之圖          4士兵上鎖之圖        56圖起點 78 圖尺寸    9購買價格   10強化價格倍率''' 
        self.SodierInfo =["Sodier",self.haveSodier,self.SodierValue,self.sodier_able_file,self.sodier_unable_file,175,200,111,106,lv_Table.solderBasicPrice,lv_Table.soliderBuyrate]
        self.ArcherInfo =["Archer",self.haveArcher,self.ArcherValue,self.archer_able_file,self.archer_unable_file,500,200,111,106,lv_Table.archerBasicPrice,lv_Table.archerBuyrate]
        self.RiderInfo =["Rider" ,self.haveRider ,self.RiderValue ,self.rider_able_file ,self.rider_unable_file ,825,200,111,106,lv_Table.riderBasicPrice,lv_Table.riderBuyrate]

        '''按鈕資訊         0買的圖      1強化的圖        23 圖尺寸  4使用者金額 '''
        self.allInfo = [self.buy_file,self.strong_file,110,46,self.userMoney]
        '''
        self.debug=0
        self.debug=self.debug+1
        print("ok",self.debug)
        '''

    def is_buy(self, obj):
        if obj is True:
            return True
        else:
            return False
        
    def buy(self,購買價格,玩家金額):

        #print("購買價格:",購買價格)

        剩餘金額 = 玩家金額 - 購買價格
        if 剩餘金額>= 0:
            玩家金額 = 剩餘金額
            return True,int(玩家金額)
        else:
            #print("餘額不足,還差","%.0f"%abs(剩餘金額),"元")
            return False,玩家金額

    def String(self,基本金額,強化金額倍率,強化等級,玩家金額):

        需花餘額 = 基本金額*(強化金額倍率**強化等級)
        #print("強化至",強化等級+1,"等級需花費%.0f"%需花餘額,"元")
        剩餘金額 = 玩家金額 - 需花餘額
        if 剩餘金額 >= 0:
            玩家金額 = 剩餘金額
            強化等級 = 強化等級+1
        #else:
            #print("餘額不足,還差","%.0f"%abs(剩餘金額),"元")

        return 強化等級,int(玩家金額)


    def setpicture(self,pictureName,x,y):
        picture=pygame.image.load(pictureName)
        picture=picture.convert_alpha()

        #(x,y)為左上角位置

        self.screen.blit(picture,(x,y))
        pygame.display.update()

    def Information(self,S,A):
        x, y = pygame.mouse.get_pos()

        if (x>=S[5] and x<=S[5]+A[2]) and (y>=S[6]+200 and y<=S[6]+200+A[3]):
            #print("玩家目前餘額:","%.0f"%A[4],"元")
            if self.is_buy(S[1]) is False:
                S[1],A[4] = self.buy(S[9],A[4])
                #print(S[0],"是否成功購買?",self.is_buy(S[1]))
                if self.is_buy(S[1]) is True:
                    S[2] = 1
                    self.textImg = self.myfont.render("Level: "+str(S[2]),1,(255,255,255))
                    self.updateScreen()
                    pygame.display.update()
                     
            else:
                S[2],A[4] = self.String(S[9],S[10],S[2],A[4])
                #print(S[0],"目前已經強化了",S[2],"等級")
                self.updateScreen()
                
        return S

    def detectWhichButton(self):
        
        #Sodier

        self.SodierInfo = self.Information(self.SodierInfo,self.allInfo)
        if (self.SodierInfo[1] is False):
            self.Info[6]  = "0"
        else:
            self.Info[6]  = "1"
        self.Info[7]  = str(self.SodierInfo[2])

        #Archer

        self.ArcherInfo = self.Information(self.ArcherInfo,self.allInfo)
        if (self.ArcherInfo[1] is False):
            self.Info[9]  = "0"
        else:
            self.Info[9]  = "1"
        self.Info[10] = str(self.ArcherInfo[2])

        #Rider       

        self.RiderInfo = self.Information(self.RiderInfo,self.allInfo)
        if (self.RiderInfo[1] is False):
            self.Info[12]  = "0"
        else:
            self.Info[12]  = "1"
        self.Info[13] = str(self.RiderInfo[2])

        #user Money

        self.Info[2] = str(self.allInfo[4])
        
        #set Value to recoder

        player.setValue(self.Info)

        '''
            if self.money >= self.sodier_cost:
                print("Sodier sold")
                self.money-=100
            '''
    def updateScreen(self):
        self.screen.blit(self.background, (0,0))
        #待處理(模組化)
        
        #SodierInfo

        if(self.SodierInfo[1] is False):

            #士兵上鎖圖

            self.setpicture(self.SodierInfo[4],self.SodierInfo[5],self.SodierInfo[6])
            self.setpicture(self.allInfo[0],self.SodierInfo[5],self.SodierInfo[6]+200)

            #購買士兵花費資訊

            self.textImg = self.myfont.render("cost: "+str(self.SodierInfo[9]),1,(255,255,255))
            self.screen.blit(self.textImg,(self.SodierInfo[5],self.SodierInfo[6]-50))
        else:

            #士兵解鎖圖

            self.setpicture(self.SodierInfo[3],self.SodierInfo[5],self.SodierInfo[6])
            self.setpicture(self.allInfo[1],self.SodierInfo[5],self.SodierInfo[6]+200)

            #士兵強化下一等級花費資訊

            self.textImg = self.myfont.render("cost: "+str(int(self.SodierInfo[9]*(self.SodierInfo[10]**self.SodierInfo[2]))),1,(255,255,255))
            self.screen.blit(self.textImg,(self.SodierInfo[5],self.SodierInfo[6]-50))

        #士兵強化等級

        self.textImg = self.myfont.render("Level: "+str(self.SodierInfo[2]),1,(255,255,255))
        self.screen.blit(self.textImg,(self.SodierInfo[5],self.SodierInfo[6]+150))


        #ArcherInfo

        if(self.ArcherInfo[1] is False):
            self.setpicture(self.ArcherInfo[4],self.ArcherInfo[5],self.ArcherInfo[6])
            self.setpicture(self.allInfo[0],self.ArcherInfo[5],self.ArcherInfo[6]+200)
            self.textImg = self.myfont.render("cost: "+str(self.ArcherInfo[9]),1,(255,255,255))
            self.screen.blit(self.textImg,(self.ArcherInfo[5],self.ArcherInfo[6]-50))
        else:
            self.setpicture(self.ArcherInfo[3],self.ArcherInfo[5],self.ArcherInfo[6])
            self.setpicture(self.allInfo[1],self.ArcherInfo[5],self.ArcherInfo[6]+200)
            self.textImg = self.myfont.render("cost: "+str(int(self.ArcherInfo[9]*(self.ArcherInfo[10]**self.ArcherInfo[2]))),1,(255,255,255))
            self.screen.blit(self.textImg,(self.ArcherInfo[5],self.ArcherInfo[6]-50))
        self.textImg = self.myfont.render("Level: "+str(self.ArcherInfo[2]),1,(255,255,255))
        self.screen.blit(self.textImg,(self.ArcherInfo[5],self.ArcherInfo[6]+150))

        #RiderInfo

        if(self.RiderInfo[1] is False):
            self.setpicture(self.RiderInfo[4] ,self.RiderInfo[5] ,self.RiderInfo[6])
            self.setpicture(self.allInfo[0],self.RiderInfo[5] ,self.RiderInfo[6]+200)
            self.textImg = self.myfont.render("cost: "+str(self.RiderInfo[9]),1,(255,255,255))
            self.screen.blit(self.textImg,(self.RiderInfo[5],self.RiderInfo[6]-50))
        else:
            self.setpicture(self.RiderInfo[3] ,self.RiderInfo[5] ,self.RiderInfo[6])
            self.setpicture(self.allInfo[1],self.RiderInfo[5] ,self.RiderInfo[6]+200)
            self.textImg = self.myfont.render("cost: "+str(int(self.RiderInfo[9]*(self.RiderInfo[10]**self.RiderInfo[2]))),1,(255,255,255))
            self.screen.blit(self.textImg,(self.RiderInfo[5],self.RiderInfo[6]-50))
        self.textImg = self.myfont.render("Level: "+str(self.RiderInfo[2]),1,(255,255,255))
        self.screen.blit(self.textImg,(self.RiderInfo[5],self.RiderInfo[6]+150))

        #User Info

        self.textImg = self.myfont.render("Welcome "+self.Info[0]+", The current balance is $"+str(int(self.allInfo[4]))+"   please press space if you want to go to last page",1,(255,255,255))
        self.screen.blit(self.textImg,(25,0))
        
    def main(self):
        self.background = pygame.image.load(self.background_file).convert()
        self.myfont = pygame.font.SysFont("monospace", 24)
        self.updateScreen()
          
        while True:            
            self.event = pygame.event.wait()
            
            if self.event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #滑鼠放開

            if self.event.type == MOUSEBUTTONUP:
                self.detectWhichButton()                    
           
            #鍵盤按下

            if self.event.type == KEYDOWN:
                if self.event.key == K_SPACE:

                        #返回上一頁
                    
                    userpage.Userpage()
            pygame.display.update()
    
        
def demo00():
    
    #產生實例

    shop = shopPage()
    shop.main()
    
if __name__=='__main__':

    demo00()
