'''
@author：KongWeiKun
@file: views.py
@time: 18-4-17 下午2:50
@contact: kongwiki@163.com
'''

from . import data

@data.route('/')
def index():
    return "<h2>这里是数据路由</h2>"