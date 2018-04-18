'''
@author：KongWeiKun
@file: views.py
@time: 18-4-17 下午2:50
@contact: kongwiki@163.com
'''
from flask import jsonify

from . import data
from .dataMysql import alarmtype_numbers,dayCount

@data.route('/')
def index():
    return "<h2>这里是数据路由</h2>" \
           "<a href='http://127.0.0.1:5000/data/alarmtypeNumbers'>事件类型发生次数统计</a><br>" \
           "<a href='http://127.0.0.1:5000/data/dayCount'>每天发生的事故</a>"


@data.route('/alarmtypeNumbers')
def alarmtypeNumbers():
    titleCount, numCount = alarmtype_numbers()
    return jsonify(titleCount=titleCount,numCount=numCount)

@data.route('/dayCounts')
def dayCounts():
    days, counts = dayCount()
    return jsonify(days = days, counts = counts)