from datetime import datetime,date
from root import Main
from flask import change_data
from time import sleep

"""课程总配置"""
start_list=[(7,50),(8,40),(9,40),(10,30),(11,20),(14,30),(15,20),(16,10),(19,30),(20,20),(21,20)]#每节课开始时间
end_list=[(8,30),(9,20),(10,20),(11,10),(12,0),(15,10),(16,0),(17,50),(20,10),(21,0),(22,30)]#每节课结束时间
class_list={0:'周一地生数英语物英体数语数',
    1:'周二物英物数地生语数物英物',
    2:'周三数英语生地英物数地生地',
    3:'周四英物数语生体地语语数语',
    4:'周五语地数物阅数英生物英英',
    5:'周六无无无无无无无无无无无',
    6:'周日无无无无无无无无地生生'}#课表

start_list=[(7,48),(8,38),(9,38),(10,28),(11,18),(14,28),(15,18),(16,8),(19,28),(20,18),(21,18)]#预备铃



if __name__ == '__main__':
    window=Main()

    today=datetime.now()
    to_week=date(today.year,today.month,today.day).weekday()
    window.today_list=change_data(class_list[to_week])
    window.local=class_list[to_week]

    window.make()
    window.win_init()

    
    num=0

    while True:
        now=(datetime.now().hour,datetime.now().minute)

        if len(end_list)==1 and now>=end_list[0]:
            window.school()

        if len(start_list)>=1:
            if now>start_list[0]:
                del(start_list[0])
                window.window.attributes('-topmost',False)
                num+=1
                window.num+=1
            elif now==start_list[0]:
                del(start_list[0])
                num+=1

            if now>end_list[0]:
                del(end_list[0])
                window.window.attributes('-topmost',True)
            elif now==end_list[0]:
                del(end_list[0])
                window.window.attributes('-topmost',True)
                window.after()


        window.light(num)
        sleep(0.1)
