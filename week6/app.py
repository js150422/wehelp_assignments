import mysql.connector
from flask import *

db = mysql.connector.connect(user='root',password='1qaz2wsx',host='localhost',database='member_system')
cursor = db.cursor()

# 初始化 Flask 伺服器
app = Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key="any string but secret"


# 首頁
@app.route("/")
def index():
    return render_template("index.html")

    
# 錯誤頁
@app.route("/error")
def error():
    message=request.args.get("msg","發生錯誤，請聯繫客服")
    return render_template("error.html",message=message)


# 註冊
@app.route("/signup",methods=["POST"])
def signup():
    # 從前端接受資料
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    

    # 撈sql資料庫
    sql_username = "SELECT username FROM member WHERE username ='%s'"%(username)
    cursor.execute(sql_username)
    result_username = cursor.fetchone()

    # 輸入的name跟username不是空值的話
    if name!="" and username!="" and password!="":
        # 搜尋註冊的usernam有沒有存在在資料庫裏面
        if result_username!=None:
            return redirect("/error?msg=帳號已經被註冊")
        # 沒有註冊過，新增mysql資料庫
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val = (name, username, password)
        cursor.execute(sql, val)
        db.commit()
        return redirect("/")
    else:
        return redirect("/error?msg=請輸入要註冊的帳號密碼")


# 登錄
@app.route("/signin", methods=["POST"])
def signin():
    # 從前端取得使用者的輸入
    username=request.form["username"]
    password=request.form["password"]


    # 連接資料庫
    sql = "SELECT name,username,password FROM member WHERE username ='%s'"%(username)
    cursor.execute(sql)
    data=cursor.fetchall()
    for user_data in data:
        name=user_data[0]
        user=user_data[1]
        key=user_data[2]

        # 登入的帳號或密碼都要等於資料庫中的資料
        if user!=username or key!=password:
            # 登入成功，在 Session 記錄會員資訊，導向到會員資料
            return redirect("/error?msg=帳號密碼輸入錯誤")
        else:
            session["name"]=name
            return redirect("/member")
    else:
        # 資料庫無資料返回
        return redirect("/error?msg=帳號密碼輸入錯誤")
# 會員頁
@app.route("/member/")
def member():
    name=session.get("name")
    if "name" in session:
        return render_template("member.html",name=name)
    else:
        return redirect("/")

# 登出
@app.route("/signout")
def signout():
    # 移除 session 中的會員資訊
    del session["name"]
    return redirect("/")

app.run(port=3000)
