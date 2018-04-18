'''
@author：KongWeiKun
@file: dataMysql.py
@time: 18-4-18 下午12:57
@contact: kongwiki@163.com
'''
from collections import Counter
import pymysql
import time


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
    cursor.close()
    return titleCount,numCount

def indexTable():
    cursor = cursors()
    querySql = 'select distinct(imei),speed,title,lat,lng,createtime from lct_event limit 10'
    cursor.execute(querySql)
    results = cursor.fetchall()
    allCountSql = 'select count(*) from lct_event'
    cursor.execute(allCountSql)
    allCount = cursor.fetchone()[0]
    titleSql = 'select count(distinct(title)) from lct_event'
    cursor.execute(titleSql)
    titleCount = cursor.fetchone()[0]
    iccardSql = 'select count(distinct(iccard)) from lct_event'
    cursor.execute(iccardSql)
    iccardCount = cursor.fetchone()[0]
    cursor.close()
    return results,allCount,titleCount,iccardCount
"""
###############################
综合分析
###############################
"""
def dayCount():
    cursor = cursors()
    querySql = ' select starttime from lct_event'
    cursor.execute(querySql)
    dayResult = cursor.fetchall()
    # print(dayResult)
    tmp = [] #暂存数据库读取的时间
    days = [] #日期列表
    counts = [] #日期values
    for item in dayResult:
        day = item[0].split(' ')[0]
        # 原始时间
        timestamp = time.mktime(time.strptime(day, '%Y-%m-%d'))
        # 数字型时间
        times = int(timestamp)
        tmp.append(times)
    dayCounts = Counter(tmp)
    dayCounts = sorted(dayCounts.items(),key=lambda x:x[0],reverse=False)
    for row in dayCounts:
        time_local = time.localtime(row[0])
        dt = time.strftime("%Y-%m-%d", time_local)
        days.append(dt)
        counts.append(row[1])
    # print(days)
    # print(counts)
    cursor.close()
    return days,counts

#车速统计
def speedCount():
    cursor = cursors()
    speeds = []
    speedNum = []
    speedSql = 'select count(speed) ,speed from lct_event group by 2'
    cursor.execute(speedSql)
    speedResult = cursor.fetchall()
    for row in speedResult:
        speeds.append(row[1])
        speedNum.append(row[0])
    cursor.close()
    return speeds,speedNum

#经纬度
def longLat():
    cursor = cursors()
    gecoords = [] #经纬度搜集
    longLatSql = 'select lng,lat from lct_event limit 100'
    cursor.execute(longLatSql)
    longLatResults = cursor.fetchall()
    for l in longLatResults:
        lng = l[0]
        lat = l[1]
        gecoord = [float(lng),float(lat)]
        gecoords.append(gecoord)
    print(gecoords)
    return gecoords


if __name__ == '__main__':
    s = longLat()

