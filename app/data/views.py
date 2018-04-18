'''
@author：KongWeiKun
@file: views.py
@time: 18-4-17 下午2:50
@contact: kongwiki@163.com
'''
from flask import jsonify

from . import data
from .dataMysql import alarmtype_numbers

@data.route('/')
def index():
    return "<h2>这里是数据路由</h2>" \
           "<a href='http://127.0.0.1:5000/data/alarmtypeNumbers'>时间类型发生次数统计</a>"

@data.route('/alarmtypeNumbers')
def alarmtypeNumbers():
    titleCount, numCount = alarmtype_numbers()
    return jsonify(titleCount=titleCount,numCount=numCount)