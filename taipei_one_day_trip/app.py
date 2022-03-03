# 內建套件載入
from flask import Response,request,Blueprint
from flask import *
import json

# 自訂義的套件載入
from admin.inquire import inquire
from admin.inquireId import inquireId




app=Flask(__name__)
app.register_blueprint(inquire)
app.register_blueprint(inquireId)


app.secret_key="any string but secret"


# json寫入後按照順序
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.config['JSON_SORT_KEYS'] = False

# Pages
@app.route("/")
def index():
	return render_template("index.html")
@app.route("/attraction/<id>")
def attraction(id):
	return render_template("attraction.html")
@app.route("/booking")
def booking():
	return render_template("booking.html")
@app.route("/thankyou")
def thankyou():

	return render_template("thankyou.html")


@app.errorhandler(500)
def server_error(e):
	r={"error":True,"message":"伺服器錯誤"}
	data=json.dumps(r,ensure_ascii=False)
	return data


app.run(port=3000)