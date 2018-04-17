'''
@author：KongWeiKun
@file: __init__.py.py
@time: 18-4-17 下午2:17
@contact: kongwiki@163.com
'''
from flask import Blueprint

main = Blueprint('main',__name__)

from . import views