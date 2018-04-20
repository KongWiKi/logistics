'''
@author：KongWeiKun
@file: views.py
@time: 18-4-17 下午2:17
@contact: kongwiki@163.com
'''
from flask import render_template, jsonify
from  . import main
from app.data.dataMysql import indexTable

@main.route('/')
def index():
    results, allCount, titleCount, iccardCount = indexTable()
    return render_template('index.html',data=results,allCount=allCount,titleCount=titleCount,iccardCount=iccardCount)

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

# @main.route('/login')
# def login():
#     return render_template('login.html')

# @main.route('/table')
# def datatable():
#     cursor.execute('select * from log where value>5')
#     return render_template('datatable.html', data=cursor.fetchall())