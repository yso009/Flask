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
        check = db.db_check(id)
        if check == False:
            db.db_insert(id)
        
    return render_template('result.html', id=id)

if __name__ =="__main__":
    app.run(debug=True)


