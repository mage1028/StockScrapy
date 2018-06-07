import pymysql
import logging
import re

def connect():
    db = pymysql.connect(host='192.168.100.103', user='root', password='root', db='stock-trade', port=3306,
                         charset='utf8')
    return db


def select_company():
    conn = connect()

    sql2='''select stockHolder from holderStatistic
    '''
    cursor = conn.cursor()
    cursor.execute(sql2)
    company = cursor.fetchall()
    conn.close()
    return company


def insert(type, name):
    conn = connect()
    sql = '''update stockHolder set Holderproporty='{0}' where stockHolder='{1}'
    '''.format(type, name)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
        logging.info('----------insert ojbk-----------------')
    except Exception as e:

        logging.exception(e)
        logging.exception(type)
        logging.exception(name)



