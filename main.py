import menu
import function

#name_card=[]

while True:
        menu.MainMenu()
        sel=int(input())
        print("您输入的选择是[%d]" % sel)
        if sel==1:
            function.makeNameCard()
        elif sel==2:
            function.ShowNameCard()
        elif sel==3:
            function.QureyCard()
        elif sel==4:
            function.RemakeCard()
        elif sel == 5:
            function.DeleteCard()
        elif sel==0:
            break
        else:
            print("输入错误，请重新输入！")

print("感谢使用该系统！再见！")