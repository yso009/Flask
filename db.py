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
    result = cursor.fetchone()

    if result == ():
        exist = False
    elif result != ():
        exist = True

    db.commit()
    db.close()

    return [result, exist]


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

def db_update(data):
    crawl_data = data
    db = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            passwd='1111',
                            db='fla',
                            charset='utf8')

    cursor = db.cursor()
    sql = """ update fla set name = %s, nickname = %s, followers=%s, followings=%s, repository=%s, introduce=%s, search_date=%s 
     where nickname = %s
    """

    cursor.execute(sql,(crawl_data[0], crawl_data[1], crawl_data[2], crawl_data[3], crawl_data[4], crawl_data[5], datetime.now(), crawl_data[1]))
    db.commit()
    db.close()