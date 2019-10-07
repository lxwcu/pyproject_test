#exercise 1
# def mailCheck(mailAddr):
#     if mailAddr.find(" ")>=0:
#         print("There's quater in mail address")
#         return "error"
#     elif not mailAddr.find("@")>=0:
#         print("There's no @ in mail address")
#         return "error"
#     elif mailAddr.find("@") == 0:
#         print("@ shouldn't at the top of mail address")
#         return "error"
#     else:
#         mailAddrSpl = mailAddr.split("@")
#         if not mailAddrSpl[1].find(".")>=0:
#             print("There's no . behind @")
#             return "error"
#         elif mailAddrSpl[1].find('.') == 0 or mailAddrSpl[1].find('.') == (len(mailAddrSpl[1])-1):
#             print("There's no letters between @ and .")
#             return "error"
#         else:
#             print(f"Email address {mailAddr} is ok!")
#
#
# mailDa = "hello.gmail@.com"
# mailCheck(mailDa)

#exercise2
# def prArr(userInfo):
#     for item in userInfo:
#         print("用户：%8s， 积分：%8.2f， 等级：%2s， 头衔：%s" %tuple(item))
#
# info = [
#     ['user1', 345.6, 12, '黄金'],
#     ['user2', 2345.6, 8, '白银'],
#     ['user3555', 55345.6, 22, '钻石'],
# ]
# prArr(info)

#exercise3
# def getNameFromStr(strs):
#     nameList = strs.split("\n")
#     for item in nameList:
#         item.strip()
#         if item == '':
#             nameList.remove(item)
#     for indx in range(len(nameList)):
#         nameList[indx] = nameList[indx].strip()
#     nameList.sort()
#     return nameList
#
# def compArr(*arrs):
#     compResult=[]
#     print(arrs[0])
#     print(arrs[1])
#     for item in arrs[0]:
#         if item not in arrs[1]:
#             compResult.append(item)
#     return compResult
#
# str1 = '''
# 熊宁
# 杰益
#
# 王伟伟
#
# 青芳
#
# 玉琴
# 焦候涛
# 莫福
# 杨高旺
# 唐欢欢
# 韩旭
# '''
#
# str2 = '''
# 焦候涛
# 熊宁
# 玉琴
#
# 骆龙
#
# 韩旭
# 杨高旺
#
# 杰益
#
# 莫福
#
# 伟伟
#
# 李福
# '''
#
# namelist1 = getNameFromStr(str1)
# namelist2 = getNameFromStr(str2)
# print(compArr(namelist1,namelist2))
# print(compArr(namelist2,namelist1))

# def dicAge(strAge):
#     dcag = {}
#     #split string into list
#     strList = strAge.split("\n")
#
#     #sort infromation list, remove null value and add useful information based on dictionary
#     print(strList)
#
#     for item in strList:
#         if item != '':
#             item = item.strip()
#             strSpList = item.split(",")
#             dcag[strSpList[0]] = int(strSpList[1])
#
#     return  dcag
#
# def sortAge(dicAg,gw):
#     upInx = []
#     downInx = []
#     print(dicAg)
#     for name,age in dicAg.items():
#         if age >= gw:upInx.append(name)
#         else:downInx.append(name)
#
#     return upInx,downInx
#
# ageTable = '''
#     诸葛亮, 28
#     刘备, 48
#     刘琦, 25
#     赵云, 32
#     张飞, 43
#     关羽, 45
#     曹操, 49
#     夏侯谆, 90
#     孙权, 20
# '''
#
# agDic = dicAge(ageTable)
# compResult = sortAge(agDic,30)
# print("30岁以上的人是：")
# for item in compResult[0]:
#     print(item)
# print("30岁以下的人是：")
# for item in compResult[1]:
#     print(item)


#exercise 4
# def printTree(height):
#     for  heig in range((height-1),-1,-1):
#         leafNum = ((heig+1)*2-1)
#         leaf = "#"*leafNum
#         lspace = ' '*(height - heig - 1)
#         print(lspace+leaf)
#
# printTree(100)

#exercise 5
# def judgeResult(handAc):
#     winList = [("石头","剪刀"),("剪刀","布"),("布","石头")]
#     loseList = [("剪刀","石头"),("布","剪刀"),("石头","布")]
#     midList = [("剪刀","剪刀"),("布","布"),("石头","石头")]
#
#     if handAc in winList:
#         return 1
#     elif handAc in loseList:
#         return -1
#     elif handAc in midList:
#         return 0
#
# def calculate_score(handAcList,name):
#     aWinTime = 0
#     aLoseTime = 0
#     aMidTime = 0
#
#
#     for item in handAcList:
#         judgeResul = judgeResult(tuple(item))
#         if judgeResul == 1:
#             aWinTime += 1
#         elif judgeResul == -1:
#             aLoseTime += 1
#         else:
#             aMidTime += 1
#
#     lastResult = [aWinTime,aMidTime,aLoseTime]
#
#     totalTime = lastResult[0]+ lastResult[1] + lastResult[2]
#     if lastResult[0] > lastResult[2]:
#         print(f"{name[0]}玩了{totalTime}局，赢了{lastResult[0]}局，平了{lastResult[1]}局，输了{lastResult[2]}局，{name[0]}胜出")
#     elif lastResult[0] < lastResult[2]:
#         print(f"{name[1]}玩了{totalTime}局，赢了{lastResult[1]}局，平了{lastResult[1]}局，输了{lastResult[0]}局，{name[1]}胜出")
#     elif lastResult[0] == lastResult[2]:
#         print(f"{name[0]}玩了{totalTime}局，赢了{lastResult[0]}局，平了{lastResult[1]}局，输了{lastResult[2]}局，{name[0]}和{name[1]}平局")
#
# handAcList = [["剪刀", "石头"], ["布", "剪刀"], ["剪刀", "剪刀"], ["石头","剪刀"], ["布","布"]]
# name = ["关羽","张飞"]
# calculate_score(handAcList,name)

#exercise 6
def dicAge(strAge):
    dcag = {}
    #split string into list
    strList = strAge.split("\n")

    #sort infromation list, remove null value and add useful information based on dictionary


    for item in strList:
        if item != '':
            item = item.strip()
            strSpList = item.split(": ")

            dcag[strSpList[0]] = int(strSpList[1])

    return  dcag

def sortAge(dicAg,gw):
    upInx = []
    downInx = []

    for name,age in dicAg.items():
        if age >= gw:upInx.append(name)
        else:downInx.append(name)

    return upInx,downInx

def culculateAge(filePath,ageGw):
    with open(filePath,"r",encoding="utf8") as infoList:
        ageTable = infoList.read()
        ageList = dicAge(ageTable)
        culResult = sortAge(ageList,ageGw)
    with open(filePath,"a",encoding="utf8")  as infoList:
        infoList.write(f"\n年龄大于{ageGw}的有：\n")
        for item in culResult[0]:
            infoList.write(item+"\n")

filePth = "D:\\0013_a1.txt"
ageGw = 50
culculateAge(filePth,ageGw)

