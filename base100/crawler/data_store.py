#!/usr/bin/python
# --*-- UTF8 --*--


import pymysql


def db_connect():
    '''
    数据库配置
    :return: con
    '''

    con = pymysql.connect(
        host='172.16.223.10',
        user='root',
        passwd='123456',
        db='crawler',
        charset='utf8'
    )
    return con


def execute_query_sql(sql):
    print('execute sql: %s' % sql)
    con = db_connect()
    try:
        cursor = con.cursor()
        cursor.execute(sql)
        con.close()
        return cursor.fetchall()

    except:
        print('error to execute the sql')
        con.close()

data = execute_query_sql("select version()")

print('Database version %s ' % data)