import lv_Table



##private hp attack move
##public islive
class rider:
    def __init__(self,l):
        self.__lv=l
    def move(self,i,Haver):
        '''
        move(欲移動的編號,Haver)
        Haver=0為左方,1為右方,-1時代表死亡
        '''
        if(Haver==0):
            return i+self.__move/50
        elif(Haver==1):
            return i-self.__move/50
        else:
            if(i-2<=0):
                self.islive=0
                return i-2
            else:
                return i-2
    def getAttack(self):
        '''
回傳攻擊值
'''
        return self.__attack;

    def attack_b(self,enemy,Haver):
        '''
attack_b(欲攻擊的敵人編號,Haver)
Haver=0為左方,1為右方
回傳值tmp在遇到敵人的情況tmp[0]會回傳false,並在tmp[1]傳出遇到了誰,反之只回傳true
        '''
        tmp=[]
        if(Haver==0):
            for i in range(0,len(enemy)):
                if(self.x+80>=enemy[i]):
                    tmp.append(False)
                    tmp.append(i)
                    return tmp
        else:
             for i in range(0,len(enemy)):
                if(self.x-80<=enemy[i]):
                    tmp.append(False)
                    tmp.append(i)
                    return tmp
        tmp.append(True)
        return tmp
    def setValue(self):
        '''
初始設定
'''
        self.type=2
        self.x=70
        self.y=680
        self.islive=1
        self.__move=60
        self.__hp=int(lv_Table.riderHPbasic*(lv_Table.riderHPrate**self.__lv))
        self.__attack=int(lv_Table.riderAttackbasic*(lv_Table.riderAttackrate**self.__lv))
    def attacked(self,att):
        '''
attacked(被傷害的數值)
當死亡時islive=-1反之持續維持1
'''
        self.__hp-=att
        if(self.__hp<=0):
            self.islive=-1
        else:
            self.islive=1
    
    def getHP(self):
        '''
取得血量
'''
        return self.__hp
    def getMove(self):
        '''
取得移動值
'''
        return self.__move

    
    

