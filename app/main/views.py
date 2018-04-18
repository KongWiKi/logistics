'''
@author：KongWeiKun
@file: views.py
@time: 18-4-17 下午2:17
@contact: kongwiki@163.com
'''
from flask import render_template, jsonify
from  . import main
from app.data.dataMysql import indexTable

import pymysql

def cursors():
    host='localhost'
    user='root'
    pwd='Hanhuan.0214'
    db='echarts'
    con=pymysql.connect(host,user,pwd,db,use_unicode=True, charset="utf8")#防止编码问题
    # con.set_charset('utf8')
    cursor=con.cursor()
    con.autocommit(True)#自动提交
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    return cursor


@main.route('/')
def index():
    results, allCount, titleCount, iccardCount = indexTable()
    return render_template('index.html',data=results,allCount=allCount,titleCount=titleCount,iccardCount=iccardCount)

@main.route('/testData')
def test():
    cursor = cursors()
    sql = 'select * from bar'
    cursor.execute(sql)
    q = cursor.fetchall()
    mon = [x[0] for x in q]
    zshui = [x[1] for x in q]
    jshui = [x[2] for x in q]
    return jsonify(mon=mon, zshui=zshui, jshui=jshui)


@main.route('/chart')
def chart():
    return render_template('chart.html')

@main.route('/table')
def table():
    return render_template('tables.html')

@main.route('/datatable')
def datatable():
    return render_template('table-list.html')

@main.route('/form')
def form():
    return render_template('form.html')

@main.route('/login')
def login():
    return render_template('login.html')

# @main.route('/table')
# def datatable():
#     cursor.execute('select * from log where value>5')
#     return render_template('datatable.html', data=cursor.fetchall())