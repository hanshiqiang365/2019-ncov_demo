#author: hanshiqiang365 （微信公众号：韩思工作室）

import time
import json
import requests
from datetime import datetime
import numpy as np
import matplotlib
import matplotlib.figure
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

#plt.rcParams['font.sans-serif'] = ['FangSong']
#plt.rcParams['axes.unicode_minus'] = False

def catch_daily():

    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts&callback=&_=%d'%int(time.time()*1000)
    data = json.loads(requests.get(url=url).json()['data'])
    data.sort(key=lambda x:x['date'])

    print(url)

    date_list = list() #
    confirm_list = list() # 确诊
    suspect_list = list() # 疑似
    dead_list = list() # 死亡
    heal_list = list() # 治愈
    for item in data:
        month, day = item['date'].split('/')
        date_list.append(datetime.strptime('2020-%s-%s'%(month, day), '%Y-%m-%d'))
        confirm_list.append(int(item['confirm']))
        suspect_list.append(int(item['suspect']))
        dead_list.append(int(item['dead']))
        heal_list.append(int(item['heal']))

    return date_list, confirm_list, suspect_list, dead_list, heal_list

def plot_daily():

    date_list, confirm_list, suspect_list, dead_list, heal_list = catch_daily() 

    plt.figure('2019-nCoV-Epidemic-Trend', facecolor='#f4f4f4', figsize=(10, 8))
    plt.title('2019-nCoV Epidemic Trend (Developed by hanshiqiang365)', fontsize=20)

    plt.plot(date_list, confirm_list, label='Confirmed Cases')
    plt.plot(date_list, suspect_list, label='Suspected Cases')
    plt.plot(date_list, heal_list, label='Healed Cases')
    plt.plot(date_list, dead_list, label='Dead Cases')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) 
    plt.gcf().autofmt_xdate()
    plt.xticks(pd.date_range('2020-01-13','2020-02-05'),rotation=90)
    plt.grid(linestyle=':') 
    plt.legend(loc='best') 
    plt.savefig('2019-nCoV-Epidemic-Trend.png') 
    #plt.show()

if __name__ == '__main__':
    plot_daily()

