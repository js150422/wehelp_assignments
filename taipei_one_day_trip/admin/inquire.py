from flask import Response,request,Blueprint
from admin.pool import pool
from mysql.connector import errors
import json
import math


inquire=Blueprint('inquire', __name__)



@inquire.route("/api/attractions")
def searchViewpointAll():
	try:
		keyword=request.args.get("keyword")
		page=request.args.get("page")
		p=int(page)

		db = pool.get_connection()
		cursor = db.cursor(dictionary=True)

		if keyword!=None:
			sql="SELECT * FROM attractions WHERE name LIKE '%s' ORDER BY `id`"%("%"+keyword+"%")
		else:
			sql="SELECT * FROM attractions ORDER BY `id`"

	
		cursor.execute(sql)
		result = cursor.fetchall()
		maxP=math.ceil(len(result)/12)-1

		g=[]
		if result!=[]:
			if p>=maxP:
				nextPage=maxP
				if  p==0:
					p1=0
					p2=11
				else:
					p1=nextPage*12
					p2=11+nextPage*12
			else:
				nextPage=p+1
				p1=nextPage+p*12
				p2=11+nextPage*12

			for i in result[p1:p2]:
				m={"id":result[0]["id"],"name":result[0]["name"],"category":result[0]["category"],"description":result[0]["description"],"address":result[0]["address"],"transport":result[0]["transport"],"mrt":result[0]["mrt"],"longitude":result[0]["longitude"],"latitude":result[0]["latitude"],"img":[result[0]["img"]]}
				g.append(m)
			r={"nextPage":nextPage,"data":g}
		else:
			r={"error":result==[],"message":"查無資料"}

		data=json.dumps(r,ensure_ascii=False)
		db.commit()
		return data
	except errors.Error as e:
		print("error",e)
	finally:
		db.close()