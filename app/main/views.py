'''
@author：KongWeiKun
@file: views.py
@time: 18-4-17 下午2:17
@contact: kongwiki@163.com
'''
from flask import render_template, jsonify
from flask_login import login_required
from  . import main
from app.data.dataMysql import indexTable

@main.route('/')
@login_required
def index():
    results, allCount, titleCount, iccardCount = indexTable()
    return render_template('index.html',data=results,allCount=allCount,titleCount=titleCount,iccardCount=iccardCount)

@main.route('/chart')
@login_required
def chart():
    return render_template('chart.html')

@main.route('/table')
@login_required
def table():
    return render_template('tables.html')

@main.route('/datatable')
@login_required
def datatable():
    return render_template('table-list.html')

@main.route('/form')
@login_required
def form():
    return render_template('form.html')

# @main.route('/author')
# def author():
#     return render_template('author.html')

# @main.route('/table')
# def datatable():
#     cursor.execute('select * from log where value>5')
#     return render_template('datatable.html', data=cursor.fetchall())