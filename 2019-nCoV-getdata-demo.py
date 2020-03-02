#author: hanshiqiang365 （微信公众号：韩思工作室）

import json, csv, requests

def get_data():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    response=requests.get(url).json()
    data = json.loads(response['data'])
    update_time=data["lastUpdateTime"]
    
    areaTree=data["areaTree"]
    with open("全国各城市病例数据.csv","w+",newline='', encoding='utf-8-sig') as csv_file:
        writer=csv.writer(csv_file)
        header=["province", "city_name", "total_confirm", "total_suspect", "total_dead", "total_heal", "today_confirm", "today_suspect", "today_dead", "today_heal","update_time"]
        writer.writerow(header)
        china_data=areaTree[0]["children"]
        for j in range(len(china_data)):
            province=china_data[j]["name"]
            city_list=china_data[j]["children"]
            for k in range(len(city_list)): 
                city_name=city_list[k]["name"]
                total_confirm=city_list[k]["total"]["confirm"]
                total_suspect=city_list[k]["total"]["suspect"]
                total_dead=city_list[k]["total"]["dead"]
                total_heal=city_list[k]["total"]["heal"]
                today_confirm=city_list[k]["today"]["confirm"]
                today_suspect=city_list[k]["total"]["suspect"]
                today_dead=city_list[k]["today"]["dead"]
                today_heal=city_list[k]["today"]["heal"]            
                data_row3=[province, city_name, total_confirm, total_suspect, total_dead, total_heal, today_confirm, today_suspect, today_dead, today_heal, update_time]
                writer.writerow(data_row3)
    
if __name__=="__main__":
    get_data()
