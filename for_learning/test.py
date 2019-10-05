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
def getNameFromStr(strs):
    nameList = strs.split("\n")
    return nameList

def 