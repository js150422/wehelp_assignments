import mysql.connector
from flask import *

db = mysql.connector.connect(user='root',password='',host='localhost',database='member_system')
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
    sql_password = "SELECT password FROM member WHERE username ='%s'"%(username)
    cursor.execute(sql_password)
    key=cursor.fetchone()


    sql_user = "SELECT username FROM member WHERE username ='%s'"%(username)
    cursor.execute(sql_user)
    user=cursor.fetchone()




    # 沒輸入就案登錄，提示[請輸入帳號密碼]
    if username!="" or password!="":
        # 用密碼撈user撈的到東西，就表示有註冊過，且用密碼撈出來的帳號跟輸入帳號一樣，代表輸入的資訊沒有問題
        if (key!=None or user!=None)and(user[0]==username and key[0]==password):
            
            # 登入成功，在 Session 記錄會員資訊，導向到會員資料
            session["username"]=username
            return redirect("/member")
        else:
            print(user)
            return redirect("/error?msg=帳號密碼輸入錯誤")
    return redirect("/error?msg=請輸入帳號密碼")


# 會員頁
@app.route("/member/")
def member():
    username=session.get("username")
    if "username" in session:
        sql_name = "SELECT name FROM member WHERE username ='%s'"%(username)
        cursor.execute(sql_name)
        name=cursor.fetchone()
        return render_template("member.html",name=name[0])
    else:
        return redirect("/")

# 登出
@app.route("/signout")
def signout():
    # 移除 session 中的會員資訊
    del session["username"]
    return redirect("/")

app.run(port=3000)
