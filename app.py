from glob import glob
from flask import Flask, make_response, render_template, request
import crawling, db
import requests
cookie_data = []

app = Flask(__name__)

@app.route('/')
def search():
    return render_template('search.html')

@app.route('/result', methods=["POST", "GET"])
def result():
    if request.method=='POST':
        id = request.form['nickname'].lower()
        search_data1 = crawling.get_data(id) # 실시간 데이터

        if search_data1 == False:
            none = False
            user_data = None
            return render_template('error.html')
            
        else:
            check = db.db_check(id)[1]
            if check == False: # db에 데이터가 없으면 
                db.db_insert(id) # db에 저장
                user_data = db.db_check(id)[0]

            else: # db에 데이터가 있다면 방금 크롤링 한 값으로 업데이트
                user_data = db.db_check(id)[0]
                db.db_update(search_data1)

        user = request.form['nickname']
        resp = make_response(render_template('result.html', user_data=user_data, search_data1 = search_data1))
        resp.set_cookie('nickname',user, max_age=None)

        return resp

            # return render_template('result.html', user_data=user_data, search_data1 = search_data1)


def cookie(nickname):
    if nickname == '':
        return cookie_data.clear()
    else:
        cookie_data.append(nickname)
        set_cookie_data = set(cookie_data)
        cookie_data_result = set_cookie_data
        return cookie_data_result


@app.route('/getcookie')
def setcookie():

    nickname = request.cookies.get('nickname')
    result = cookie(nickname)
    print(result)
    if len(result) == 0:
        result = 'No Data'
    # cookie_data.append(nickname)
    # set_cookie_data = set(cookie_data)
    # cookie_data_result = set_cookie_data
    
    return render_template('getcookie.html', li = result)

@app.route('/refresh')
def delete_cookie():
    nickname = ''
    result = cookie(nickname)
    return render_template('getcookie.html', li='No Data')

    


if __name__ =="__main__":
    app.run(debug=True)


