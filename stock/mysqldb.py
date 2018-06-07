import pymysql
import logging


def connect():
    db = pymysql.connect(host='192.168.100.103', user='root', password='root', db='stock-trade', port=3306,
                         charset='utf8')
    return db


def select_company(x):
    conn = connect()
    sql = '''select stockHolder from holderStatistic order by id limit {0},1
    '''.format(x)
    cursor = conn.cursor()
    cursor.execute(sql)
    company = cursor.fetchall()[0][0]
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
