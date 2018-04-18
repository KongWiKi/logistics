'''
@author：KongWeiKun
@file: dataMysql.py
@time: 18-4-18 下午12:57
@contact: kongwiki@163.com
'''
import pymysql

def cursors():
    host='localhost'
    user='root'
    pwd='Hanhuan.0214'
    db='logistics'
    con=pymysql.connect(host,user,pwd,db,use_unicode=True, charset="utf8")#防止编码问题
    # con.set_charset('utf8')
    cursor=con.cursor()
    con.autocommit(True)#自动提交
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    return cursor

def alarmtype_numbers():
    cursor = cursors()
    titleCount = []
    numCount = []
    alarmtypeNumbersSql = ' select count(alarmtype) as numbers,title from lct_event group by 2'
    cursor.execute(alarmtypeNumbersSql)
    results = cursor.fetchall()
    for items in results:
        title = items[1]
        num = items[0]
        titleCount.append(title)
        numCount.append(num)
    return titleCount,numCount

if __name__ == '__main__':
    s = alarmtype_numbers()
    print(s[0])
