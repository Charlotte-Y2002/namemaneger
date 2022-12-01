import menu
import time

card={}
card_name=[]
def makeNameCard():
    menu.Menu1()
    print("请输入姓名：")
    name=input()
    print("请输入年龄：")
    age=input()
    print("请输入电话：")
    phone=input()

    card={"name":name,
        "age":age,
        "phone":phone}

    card_name.append(card)
    print("新建%s名片成功！"%name)
    time.sleep(3)
    #return card_name

def ShowNameCard():
    menu.Menu2()
    if(card_name==[]):
        print("-"*50)
        print("不好意思!此列表暂时为空")
        print("-"*50)
        time.sleep(3)
    else:
        for title in ["姓名","年龄","电话"]:
            print(title,end="\t\t")
        print("")
        print("="*50)
        for card in card_name:
            print("%s\t\t%s\t\t%s"%(card['name'],card['age'],card['phone']))
        print("")
        time.sleep(3)

def QureyCard():
    menu.Menu3()
    if card_name==[]:
        print("-"*50)
        print("不好意思，表格为空")
        print("-" * 50)
        time.sleep(3)
    else:
        Q_name = input()
        for card in card_name:
            if card["name"] == Q_name:
                print("查找成功！")
                print("=" * 50)
                print("%s\t\t%s\t\t%s" % (card['name'], card['age'], card['phone']))
                time.sleep(3)
                break
        else:
            print("没有查到该用户！")
            time.sleep(3)

def RemakeCard():
    menu.Menu4()
    if card_name==[]:
        print("-"*50)
        print("不好意思，表格为空")
        print("-" * 50)
        time.sleep(3)
    else:
        R_name=input()
        for card in card_name:
            if card["name"]==R_name:
                print("请输入修改的姓名、年龄、电话")
                print("-"*50)
                print("请输入姓名：")
                card['name']=input()
                print("请输入年龄：")
                card['age'] = input()
                print("请输入电话：")
                card['phone'] = input()
                print("修改%s名片成功！" % R_name)
                time.sleep(3)
                break
        else:
            print("没有该用户哦！")
            time.sleep(3)

def DeleteCard():
    menu.Menu5()
    if card_name==[]:
        print("-"*50)
        print("不好意思，表格为空")
        print("-" * 50)
        time.sleep(3)

    else:
        D_name=input()
        for card in card_name:
            if card["name"]==D_name:
                card_name.remove(card)
                print('已删除该用户')
                time.sleep(3)
                break
        else:
            print("没有该用户哦！")
            time.sleep(3)


