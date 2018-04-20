'''
@author：KongWeiKun
@file: views.py
@time: 18-4-20 下午3:25
@contact: kongwiki@163.com
'''
import uuid

from  flask import render_template, url_for, request, redirect, flash
from flask_login import login_user,login_required

from . import user
from .forms import  LoginForm,RegistrationForm
from app.models import  User
from app import db


@user.route('/')
def index():
    return "<h1>--><--</h1>"


@user.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user,form.remember_me) # 如果密码正确 调用login_user 在用户会话中会标记为已登录
        # print(form.username.data)
        # print(form.password.data)
        return "<h1>你好</h1>"
    return render_template('/login/login.html',form=form)

@user.route('/register',methods=['POST','GET'])
def register():
    form =RegistrationForm()
    if form.validate_on_submit():
        user = User(id=str(uuid.uuid4()),username=form.username.data,
                                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("You can now Login")
        return '<h1>注册成功</h1>'
    return render_template('/login/register.html',form=form)

@user.route('/finall')
def finall():
    return "<h1>-><-</h1>"
