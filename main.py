import PySimpleGUI as sg
import random
from operator import length_hint
from utils import API#call the utils files

my_API = API()# API class

sg.set_options(font=('Arial Bold', 16))#set GUI style

city_get = sg.Input(expand_x=True)
province_get = sg.Input(expand_x=True)
#set input
weather_button = sg.Button('天气查询',size=(10,1))
scenic_button = sg.Button('景区查询',size=(10,1))
news_button = sg.Button('资讯查询',size=(10,1))
clean_button = sg.Button('清除显示',size=(10,1))
#set button
prompt_box = sg.Text('选择准备旅游的城市吧!')
result_text = sg.Multiline(justification='center',size=(60,7.5))
#set text
layout = [
[sg.Text('目标省份:', size=(10,1)),province_get],
[sg.Text('目标城市:', size=(10,1)),city_get],
[prompt_box],
[result_text],
[weather_button,news_button,scenic_button,clean_button]
]
#position the components in the layout
window =sg.Window('旅游小助手', layout, size=(620,350))
#set window
while True:
    #continuously monitor window information change
    event, value = window.read()
    if event == sg.WIN_CLOSED: break

    if event == '天气查询':
        temperature,humidity,info,direct,power,aqi=my_API.weather(city_get.get())
        #invoke weather() to assign values
        if temperature==999:
            result_text.update('请求失败，请输入合法值')
            #not valid input
        else:
            result_text.update('温度:'+str(temperature)+'\n'+'湿度:'+str(humidity)+'\n'+'天气:'+str(info)+'\n'+'风向:'+str(direct)+'\n'+'风力:'+str(power)+'\n'+'空气质量:'+str(aqi))
            #update the information

    if event == '景区查询':
        scenic_list= my_API.scenic_spot(city_get.get())
        if scenic_list == []:
            result_text.update('请求失败，请输入合法值')
        else:
            scenic_str = ''
            for i in range(0,length_hint(scenic_list['list'])):
                scenic_str = scenic_str+scenic_list['list'][i]['name']+'\n'
            #concatenate the contents of a list into a string
            result_text.update(scenic_str)

    if event == '资讯查询':
        news_list = my_API.news(province_get.get())
        if news_list == []:
            result_text.update('请求失败，请输入合法值')
        else:
            random_num = int(random.uniform(0,int(length_hint(news_list['list']))))
            #randomly return a news from the list
            result_text.update('新闻时间:'+news_list['list'][random_num]['ctime']+'\n'+news_list['list'][random_num]['title']+'\n'+news_list['list'][random_num]['url']+'\n'+'新闻来源:'+news_list['list'][random_num]['source'])

    if event == '清除显示':
        result_text.update('')
        # clean the text
window.close()
