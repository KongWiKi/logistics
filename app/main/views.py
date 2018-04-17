'''
@author：KongWeiKun
@file: views.py
@time: 18-4-17 下午2:17
@contact: kongwiki@163.com
'''
from flask import render_template

from  . import main


@main.route('/')
def index():
    return render_template('index.html')