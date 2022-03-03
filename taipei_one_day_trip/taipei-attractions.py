import json
import mysql.connector


db = mysql.connector.connect(user='root',password='',host='localhost',database='one_day_trip')
cursor = db.cursor()


with open('data/taipei-attractions.json',encoding = 'utf-8') as file:
    result=json.load(file)
    Q=len(result["result"]["results"])



    for i in range(0,Q,1):
        name=result["result"]["results"][i]["stitle"]
        category=result["result"]["results"][i]["CAT2"]
        description=result["result"]["results"][i]["xbody"]
        address=result["result"]["results"][i]["address"].split(' ')[2]
        transport=result["result"]["results"][i]["info"]
        mrt=result["result"]["results"][i]["MRT"]
        longitude=result["result"]["results"][i]["longitude"]
        latitude=result["result"]["results"][i]["latitude"]
        
        file=result["result"]["results"][i]["file"].split('https')[1:]
        file_check=[]
        for m in file:
            file_c='http'+m.lower()
            if 'jpg' in file_c or 'png' in file_c:
                file_check.append(file_c)
        img="".join(file_check)
        mySql_insert_query = """INSERT INTO attractions (name,category,description,address,transport,mrt,longitude,latitude,img) 
                                VALUES (%s, %s,%s, %s, %s,%s, %s, %s, %s) """

        record = (name,category,description,address,transport,mrt,longitude,latitude,img)
        cursor.execute(mySql_insert_query, record)
        db.commit()

#from pandas import json_normalize
#df=json_normalize(data['result']['results'])
