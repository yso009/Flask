import pymysql
import crawling
from datetime import datetime

def db_check(id):

    db = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            passwd='1111',
                            db='fla',
                            charset='utf8')

    cursor = db.cursor()
    sql = """ select * from fla where nickname = %s
             """

    cursor.execute(sql, id)
    result = cursor.fetchall()

    if result == ():
        result = False
    else:
        result = True

    db.commit()
    db.close() 
    return result


def db_insert(data):
    crawl_data = crawling.get_data(data)

    db = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            passwd='1111',
                            db='fla',
                            charset='utf8')

    cursor = db.cursor()
    sql = """ insert into fla(name, nickname, followers, followings, repository, introduce, search_date) 
                values (%s,%s,%s,%s,%s,%s,%s)
             """

    cursor.execute(sql,(crawl_data[0], crawl_data[1], crawl_data[2], crawl_data[3], crawl_data[4], crawl_data[5], datetime.now()))

    db.commit()
    db.close()
