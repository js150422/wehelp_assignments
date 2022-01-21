from flask import Flask # 載入 Flack
from flask import request # 載入 Request 物件
from flask import render_template # 載入render_template函式
from flask import redirect # 載入 redirect
from flask import session
app=Flask(__name__, static_url_path="/") 

app.secret_key="any string but secret" # 設定 Session的密鑰
# 網站的首頁
@app.route("/")
def index():
    return render_template("week4.html")


@app.route("/signin", methods=["POST"])
def singnin():
    account=request.form["account"]
    key=request.form["key"]
    if account!="" and key!="":
        if account=="test" and key=="test":
            session["account"]=account # session["欄位名稱"]=資料
            return redirect("/member/")
        else:
            return redirect("/error/?msg=帳號或密碼輸入錯誤")
    else:
         return redirect("/error/?msg=請輸入帳號密碼")
       
    
@app.route("/member/")
def member():
    account=session.get("account")
    if "account" in session:
        return render_template("member.html",account=account)
    else:
        return redirect("/")
@app.route("/signout")
def singout():
    out=session.clear()
    return redirect("/")



@app.route("/error/")
def error():
    if "account" not in session:
        message=request.args.get("msg","請輸入帳號、密碼")
        return render_template("error.html",message=message)
    else:
        message=request.args.get("msg","帳號、或密碼輸入錯誤")
        return render_template("error.html",message=message)
    
   
# 啟動伺服器在 Port 3000
app.run(port=3000) 
