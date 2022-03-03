from flask import Response,request,Blueprint
from admin.pool import pool
from mysql.connector import errors
import json

inquireId=Blueprint('inquireId', __name__)


@inquireId.route("/api/attractions/<n>")
def searchViewpointById(n):
	try:
		db = pool.get_connection()
		cursor = db.cursor(dictionary=True)
		sql="SELECT * FROM attractions WHERE id='%s'"%(n)
		cursor.execute(sql)
		result = cursor.fetchall()
		if cursor!=None:
			m={"data":{"id":result[0]["id"],"name":result[0]["name"],"category":result[0]["category"],"description":result[0]["description"],"address":result[0]["address"],"transport":result[0]["transport"],"mrt":result[0]["mrt"],"longitude":result[0]["longitude"],"latitude":result[0]["latitude"],"img":[result[0]["img"]]}}
			data=json.dumps(m,ensure_ascii=False)
			db.commit()
			return data
		else:
			r={"error":result==None,"message":"景點編號不正確"}
			data=json.dumps(r,ensure_ascii=False)
			return Response(response=data, status=400)
	except errors.Error as e:
		print("Error",e)
	finally:
		db.close()