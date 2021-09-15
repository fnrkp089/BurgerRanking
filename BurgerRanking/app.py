from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.burger_list

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mainpage', methods=['GET'])
def burgers_list():
    burgers = list(db.hamburger.find({},{'_id':False}).sort('like', -1))
    return jsonify({'result':'success', 'all_burgers': burgers})


# 리뷰작성
@app.route('/comment', methods=['POST'])
def burgers_review():
    comment_receive = request.form['comment_give']

    db.hamburger.insert_one(comment_receive)

    return jsonify({'result':'success'})

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