import random

filePath ="idiom.txt"
AutoChoice=""
GameOver = False
#read the txt file
def readFile(x):
    
    #open the text file
    with open(filePath,"r") as fp:
        #read line 
        for i in set(fp.readlines()):
            #if enter input is same as the idiom
            if x == i.strip(): #strip > Remove spaces at the beginning and at the end of the string
                #if enter input can be find in the file
                
                return True
        #Can not find in the file for input value             
        return False

def Validation(First,Second):
    """如果第二个成语第一个字 不是等于第一个成语最后一个字 或者 第二个成语不是4个字"""
    if Second[0] != First[-1] or len(Second)!=4:
        print("不符合要求")
        #not meet the requirment
        return False
    #meet the requirment
    return True
def CreateIdiom():
    """随机成语"""
    
    #ramdom 
    with open(filePath,'r') as f:
        # Random select one of the idiom
        AutoChoice = random.choice(f.readlines()) [:-1] #remove the \n  \n Automatic generated
        print(AutoChoice)
        return AutoChoice

def PlayWithAI():
    GameOver =False
    #Keep running until game over is true
    while (GameOver==False):
        AutoChoice = CreateIdiom()
        answers  = input("请输入成语:")
    
        # unable to find in the file
        if readFile(answers)== False:
            print("成语不存在")
            GameOver = True
        # able to find in the file 
        if readFile(answers)== True:
            print("成语存在")
            
        if Validation(AutoChoice,answers):
            print("正确")
        else:
            print("你输了！")
            GameOver = True
def FindIdiom():
    text = input("请输入一个字来找相同的第一个成语字\n")
        #open file
    with open(filePath,"r") as fp:
        #read line 
        for i in set(fp.readlines()):
            #if input is same as the idiom first word print that idiom
            if text ==i.strip()[0]:
                print(i.strip())
def main():
    question = input("成语接龙:y 查询成语:x\n")
    if question =="y":
        PlayWithAI()
    if question =='x':
        FindIdiom()
#Run the program
main()

