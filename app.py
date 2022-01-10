from flask import Flask, render_template, request
import crawling, db
import requests

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
            
            return render_template('result.html', user_data=user_data, search_data1 = search_data1)

if __name__ =="__main__":
    app.run(debug=True)


