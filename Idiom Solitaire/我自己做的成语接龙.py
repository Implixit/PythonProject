import random

filePath ="idiom.txt"
AutoChoice=""
#阅读文件而且找那文件
def readFile(x):
    
    #打开文件
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
def mian():
    AutoChoice = CreateIdiom()
    answers  = input("请输入成语:")
    if Validation(AutoChoice,answers):
        print("正确")
    # unable to find in the file
    if readFile(answers)== False:
        print("成语不存在")
        return 0
    # able to find in the file 
    if readFile(answers)== True:
        print("成语存在")
        return 0 

#Run the program
mian()

