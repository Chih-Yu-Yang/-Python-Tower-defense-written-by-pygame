
def getValue(targetFile):
    file = open(targetFile, 'r', encoding = 'UTF-8')
    num=0
    done=0
    ValueArray=[]
    while not done:
        tmp=file.readline()
        ValueArray.insert(num,tmp[tmp.find("=")+1:].strip())
        if(tmp == ''):
            done=1
        num+=1
    return ValueArray
    file.close()
def setValue(Info):
    file = open("data/recoder.txt", 'w', encoding = 'UTF-8')
    file.write('PlayerName='+Info[0]+"\n")
    file.write('PlayerLv='+Info[1]+"\n")
    file.write('PlayerMoney='+Info[2]+"\n")
    file.write('PlayerExp='+Info[3]+"\n")
    file.write('PlayerPassed='+Info[4]+"\n")
    file.write('levels='+Info[5]+"\n")
    file.write('solider='+Info[6]+"\n")
    file.write('slv='+Info[7]+"\n")
    file.write('sr='+Info[8]+"\n")
    file.write('archer='+Info[9]+"\n")
    file.write('alv='+Info[10]+"\n")
    file.write('ar='+Info[11]+"\n")
    file.write('rider='+Info[12]+"\n")
    file.write('rlv='+Info[13]+"\n")
    file.write('rr='+Info[14]+"\n")
    file.close()
def setInitial(name):
    file = open("data/recoder.txt", 'w', encoding = 'UTF-8')
    file.write("PlayerName="+name+"\n")
    file.write("PlayerLv=1\n")
    file.write("PlayerMoney=1000\n")
    file.write("PlayerExp=0\n")
    file.write("PlayerPassed=0\n")
    file.write("levels=3\n")
    file.write("solider=1\n")
    file.write("slv=1\n")
    file.write("sr=40\n")
    file.write("archer=0\n")
    file.write("alv=0\n")
    file.write("ar=150\n")
    file.write("rider=0\n")
    file.write("rlv=0\n")
    file.write("rr=80\n")
    file.close()
