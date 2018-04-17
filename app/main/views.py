'''
@author：KongWeiKun
@file: views.py
@time: 18-4-17 下午2:17
@contact: kongwiki@163.com
'''
from flask import render_template
from  . import main

import pymysql
host='localhost'
user='root'
pwd='Hanhuan.0214'
database='webLog'
con=pymysql.connect(host,user,pwd,database)
cursor=con.cursor()


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/chart')
def chart():
    return render_template('chart.html')

@main.route('/login')
def login():
    return render_template('login.html')

# @main.route('/table')
# def datatable():
#     cursor.execute('select * from log where value>5')
#     return render_template('datatable.html', data=cursor.fetchall())