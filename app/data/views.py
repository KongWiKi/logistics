'''
@author：KongWeiKun
@file: views.py
@time: 18-4-17 下午2:50
@contact: kongwiki@163.com
'''
import json

from flask import jsonify

from . import data
from .dataMysql import alarmtype_numbers,dayCount,speedCount,longLat,calenderCount

@data.route('/')
def index():
    return "<h2>这里是数据路由</h2>" \
           "<a href='http://127.0.0.1:4000/data/alarmtypeNumbers'>事件类型发生次数统</a><br>" \
           "<a href='http://127.0.0.1:4000/data/dayCounts'>每天发生的事故</a><br>" \
           "<a href='http://127.0.0.1:4000/data/speedCounts'>车速统计</a><br>" \
           "<a href='http://127.0.0.1:4000/data/lngLat'>经纬度</a><br>" \
           "<a href='http://127.0.0.1:4000/data/calendarData'>日历数据</a><br>"\

@data.route('/alarmtypeNumbers')
def dataAlarmtypeNumbers():
    titleCount, numCount = alarmtype_numbers()
    return jsonify(titleCount=titleCount,numCount=numCount)

@data.route('/dayCounts')
def dayCounts():
    days, counts = dayCount()
    return jsonify(days = days, counts = counts)

@data.route('/speedCounts')
def speedCounts():
    speeds, speedNum = speedCount()
    return jsonify(speed = speeds, speedNum = speedNum)

@data.route('/lngLat')
def lngLat():
    gecoords = longLat()
    return json.dumps(gecoords)

@data.route('/calendarData')
def calendarData():
    calendarResule = calenderCount('2016')
    return jsonify(calendarResule)