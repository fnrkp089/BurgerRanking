import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from pymongo import MongoClient

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static"

SECRET_KEY = 'SPARTA'

client = MongoClient('localhost', 27017)
db = client.project

@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        return render_template('index.html', user_info=user_info['username'])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

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


@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    name_receive = request.form['name_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,
        "password": password_hash,
        "profile_name": name_receive
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})

@app.route('/mainpage', methods=['GET'])
def burgers_list():
    target = request.args.get('type');
    if target is not None:
        burgers = list(db.hamburger.find({'brand' : target}, {'_id': False}).sort('like', -1))
    else:
        burgers = list(db.hamburger.find({},{'_id':False}).sort('like', -1))
    return jsonify({'result':'success', 'all_burgers': burgers})

#리뷰 불러오기
@app.route('/get_comment', methods=['GET'])
def comment_list():
    burgerid = request.args.get('burgerComment')
    print(burgerid)
    comment = list(db.review.find({'burger_id': burgerid} , {'_id':False}))

    return jsonify({'result': 'success', 'commentList': comment})

# 리뷰작성
@app.route('/comment', methods=['POST'])
def burgers_review():
    try:
        comment_receive = request.form['comment_give']
        burgerId = request.form['burgerId']
        username = request.form['username']
        commentid = request.form['comment_id']
        doc = {
            'comment_id': commentid,
            'burger_id': burgerId,
            'username' : username,
            'comment': comment_receive,
        }
        db.review.insert_one(doc)
        return jsonify({'result':'success'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


# 리뷰 수정
@app.route('/comment_edit', methods=['POST'])
def review_edit():
    username_receive = request.form['username_give']
    comment_receive = request.form['comment_give']
    db.review.update_one({'name':username_receive}, {'$set':{'comment':comment_receive}})
    return jsonify({'result': 'success'})

# 리뷰 삭제
@app.route('/comment_delete', methods=['POST'])
def review_delete():
    print("삭제")
    comment_receive = request.form['comment_give']
    db.review.delete_one({"comment_id":comment_receive})

    return jsonify({'result': 'success'})


# 좋아요
@app.route('/like', methods=['POST'])
def burgers_like():
    name_receive = request.form['name_give']
    like = db.hamburger.find_one({'name':name_receive})
    new_like = like['like']+1

    db.hamburger.update_one({'name':name_receive}, {'$set':{'like': new_like}})
    return jsonify({'result':'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)