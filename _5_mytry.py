from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import make_response

app = Flask(__name__)

#리스트생성
db_board = []
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/setcookie" ,methods =['POST'])
def setcookie():
    user = request.form['nm']
        
    resp = make_response(redirect("/success"))
    resp.set_cookie('userID', user)
    return resp

@app.route("/success")
def success():
    return "성공적으로 등록 되었습니다."

@app.route("/check")
def check():
    user = request.cookies.get("userID")
    if user == "wlgud0402":
        return "ok"
    else:
        return "유저값이 일치하지 않습니다."

@app.route("/uni")
def uni():
    return render_template("main.html")

@app.route("/market")
def market():
    return render_template("market.html")



@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/dd")
def dd():
    return render_template("dd.html")

#게시판 board를 생성 >>board로 render_template
@app.route("/board")
def board():
    global db_board     #db_board를 외부에서 가져옴
    return render_template(
        "board.html",
        boardList = db_board,   #boardList에 db_board를 넣어줌
    )

#내가 글쓰는 페이지
@app.route("/test")
def test():
    print("포스트임")
    return render_template("post.html")     #post로 render

#글이 써지고서 어떻게 적용되는지를 보여준다, 이전에 post.html을 봐서 흐름 이해
@app.route("/post", methods=['POST'])
def post():
    value = request.form['test']
    db_board.append(value)
    return redirect('/board') 

db_bag=[]
@app.route("/bag", methods=['POST'])

if __name__ == "__main__":
    app.run(port=3001)
