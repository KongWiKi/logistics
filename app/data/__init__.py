'''
@author：KongWeiKun
@file: __init__.py.py
@time: 18-4-17 下午2:50
@contact: kongwiki@163.com
'''
from flask import Blueprint

data = Blueprint('data',__name__)

from . import views