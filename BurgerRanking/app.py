import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static"

SECRET_KEY = 'SPARTA'

#client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.project

#페이지 접속시 로그인 여부 확인
@app.route('/')
def home():
    #쿠키로 부터 토큰 가져오기
    token_receive = request.cookies.get('mytoken')
    #JWT 디코드하여 paylod에 정보 저장
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        #로그인 정보로 사용자의 아이디를 가져옴
        user_info = db.users.find_one({"username": payload["id"]})
        return render_template('index.html', user_info=user_info['username'])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

#로그인 페이지 접속시
@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

#회원가입 API
@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    name_receive = request.form['name_give']
    #입력받은 비밀번호를 해시값으로 저장.
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,
        "password": password_hash,
        "profile_name": name_receive
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})

#아이디 중복확인 체크 API
@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})

#로그인 후, 버거 조회 API
@app.route('/mainpage', methods=['GET'])
def burgers_list():
    #어떤 브랜드의 버거를 가져올지 'TPYE'이란 변수명에 담겨진 값을 가져와 비교
    target = request.args.get('type');

    #만일 브랜드 버거가 없는. 즉 모든 버거를 가져오라는 이벤트일 경우 모두 가져오고 그렇지 않을경우 브랜드를 조회하여 가져온다.
    if target is not None:
        burgers = list(db.hamburger.find({'brand': target}, {'_id': False}).sort('like', -1))
    else:
        burgers = list(db.hamburger.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'result': 'success', 'all_burgers': burgers})


# 리뷰 불러오기
@app.route('/get_comment', methods=['GET'])
def comment_list():
    #해당하는 버거의 고유아이디와 고유 코멘트를 가져온다.
    burgerid = request.args.get('burgerComment')
    comments = list(db.review.find({'burger_id': burgerid}))
    for comment in comments:
        comment["_id"] = str(comment["_id"])
    return jsonify({'result': 'success', 'commentList': comments})


# 리뷰작성
@app.route('/comment', methods=['POST'])
def burgers_review():
    try:
        #입력받은 코멘트와, 사용자의 아이디 그리고 해당되는 버거 아이디를 배열에 저장하고 해당 배열을 데이터 베이스에 입력한다.
        comment_receive = request.form['comment_give']
        burgerId = request.form['burgerId']
        username = request.form['username']
        doc = {
            'burger_id': burgerId,
            'username': username,
            'comment': comment_receive,
        }
        db.review.insert_one(doc)
        return jsonify({'result': 'success'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


# 리뷰 삭제
@app.route('/comment_delete', methods=['POST'])
def review_delete():
    #해당 리뷰를 작성한 작성자일 경우, 코멘트의 고유아이디값을 조회해 해당 이벤트가 일어난 코멘트값만 삭제한다.
    comment_receive = request.form['comment_give']
    db.review.delete_one({'_id': ObjectId(comment_receive)})
    return jsonify({'result': 'success'})


# 좋아요
@app.route('/like', methods=['POST'])
def burgers_like():
    #이벤트가 발생한 버거의 이름으로 조회하여 해당 버거의 좋아요 갯수를 1 증가시킨다.
    name_receive = request.form['name_give']
    like = db.hamburger.find_one({'name': name_receive})
    new_like = like['like'] + 1

    db.hamburger.update_one({'name': name_receive}, {'$set': {'like': new_like}})
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
