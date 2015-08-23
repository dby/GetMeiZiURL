#coding: utf-8

import sae
import json
import MySQLdb
from datetime import datetime
from hostgirls import app
from flask import Flask, g, request, abort, jsonify

from .models import MeiZiModel
from .database import db
from meiziSpider import MeiZiSpider

from sae.const import (MYSQL_HOST, MYSQL_HOST_S, MYSQL_PORT,
    MYSQL_USER, MYSQL_PASS, MYSQL_DB
)

@app.route('/')
def hello():
    return app.config['SQLALCHEMY_DATABASE_URI']

'''
    创建数据库
'''
@app.route('/initTable/')
def initSQL():
    db.create_all()
    return "success"


'''
    删除表
'''
@app.route('/dropTable/')
def removeSQL():
    db.drop_all()
    return "success"

'''
    向数据库中添加一列妹子的信息
'''
@app.route('/add/')
def addOne():
    meizis = MeiZiSpider().getMeiZiAtPage(2)
    for meizi in meizis:
        m = MeiZiModel(meizi["imgsrc"], meizi["title"], meizi["topiclink"], meizi["startcount"])
        db.session.add(m)
        db.session.commit()

    return "success"

'''
    获取妹子的信息
'''
@app.route('/meizi/', methods=['GET'])
def getMeiZi():
    if request.method == 'GET':
        lim = int(request.args.get('limit', 30))
        off = int(request.args.get('offset',0))
        data = MeiZiModel.query.order_by(MeiZiModel.id).limit(lim).offset(off)
        return jsonify(error = {"error_code":"1", "error_msg": "success"}, res = [i.serialize for i in data]) 

@app.before_request
def before_request():
    db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS,
    MYSQL_DB, port=int(MYSQL_PORT))

@app.teardown_request
def teardown_request(exception):
    if app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']:
        if exception is None:
            db.session.commit()
    db.session.remove()
    return exception
