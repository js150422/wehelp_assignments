import urllib.request as request
import json 
import csv

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) # 利用 json 模組處理json資料格式
    n=0
    with open("veiwpoint.csv", mode="a",newline='', encoding="utf-8")as file:
        csvWriter = csv.writer(file)  
        while n<len(data["result"]["results"]):
            
            name=data["result"]["results"][n]["stitle"]
            address=data["result"]["results"][n]["address"].split(' ')[2][0:3]
            longitude=data["result"]["results"][n]["longitude"]# 經度
            latitude=data["result"]["results"][n]["latitude"]# 緯度
            img="http"+data["result"]["results"][n]["file"].split('https')[1]# 圖片只要第一張       
            viewpoint=[name,address,longitude,latitude,img]
            csvWriter.writerow(viewpoint)
            n+=1
        
    with open("veiwpoint.csv", mode="r", encoding="utf-8")as outfile:
        final=outfile.read()
        print(final)