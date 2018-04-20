'''
@author：KongWeiKun
@file: __init__.py.py
@time: 18-4-20 下午3:08
@contact: kongwiki@163.com
'''
from flask import Blueprint

user = Blueprint('user',__name__)

from . import views