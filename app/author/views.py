'''
@author：KongWeiKun
@file: views.py
@time: 18-4-20 下午3:25
@contact: kongwiki@163.com
'''
import uuid

from  flask import render_template, url_for, request, redirect, flash
from flask_login import login_user,login_required,logout_user

from . import author
from .forms import  LoginForm,RegistrationForm
from app.models import  User
from app import db


@author.route('/')
def index():
    return "<h1>--><--</h1>"\
            "<h2>这里是登录界面<br></h1>"\
            "<h2>登录链接--<a href='/login'>登录</a></h2>"


@author.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user,form.remember_me) # 如果密码正确 调用login_user 在用户会话中会标记为已登录
        print(form.username.data)
        print(form.password.data)
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('login.html',form=form)

@author.route('/register',methods=['POST','GET'])
def register():
    form =RegistrationForm()
    if form.validate_on_submit():
        user = User(id=str(uuid.uuid4()),username=form.username.data,
                                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("You can now Login")
        return redirect(url_for('main.index'))
    return render_template('sign-up.html',form=form)

@author.route('/logout')
@login_required
def logout():
    logout_user()
    flash("已成功退出")
    return redirect(url_for('/login'))


@author.route('/finall')
def finall():
    return "<h1>-><- -><-</h1>"
