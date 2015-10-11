#coding: utf-8

import sae
import json
import MySQLdb
from datetime import datetime
from hostgirls import app
from flask import Flask, g, request, abort, jsonify

from .models import *
from .database import db
from meiziSpider import MeiZiSpider

from sae.const import (MYSQL_HOST, MYSQL_HOST_S, MYSQL_PORT,
    MYSQL_USER, MYSQL_PASS, MYSQL_DB
)

@app.route('/')
def hello():
    return "welcome to HostGirls"

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
FUCTION:    向数据库中添加200个妹子的信息
NOTE:       初始化完成之后不需要在调用，内部接口
    
'''
@app.route('/initData/')
def addMeiZiByCid():
    for i in range(1, 15)[::-1]:
        meizis = MeiZiSpider().getMeiZiAtPage(i, 1)[::-1]
        for meizi in meizis:
            m = MeiZiModel(meizi["imgsrc"], meizi["title"], meizi["topiclink"], meizi["startcount"])
            db.session.add(m)
            try:
                db.session.commit()
            except:
                db.session.rollback()

    return "success"

'''
    定时更新大胸妹
'''
@app.route('/updateBigChest')
def updateBigChestMeiZi():
    bigChestMeiZi = MeiZiSpider().getMeiZiAtPage(1, 2)[::-1]
    meiZiInMySQL = BigChestModel.query.order_by("id DESC").limit(30)
    
    for mz in bigChestMeiZi:
        flag = 0
        for bcm in meiZiInMySQL:
            if bcm.imgsrc == mz["imgsrc"]:
                flag = 1
                break;
        if flag == 0:
            mmzz = BigChestModel(mz["imgsrc"], mz["title"], mz["topiclink"], mz["startcount"])
            db.session.add(mmzz)
            try:
                db.session.commit()
            except:
                db.session.rollback()
    return "update BigChestMeiZi SUCCESS"
            
'''
    定时更新丝袜妹
'''
@app.route('/updateBlackStocking')
def updateBlackStockingMeiZi():
    blackStockingMeiZi = MeiZiSpider().getMeiZiAtPage(1, 7)[::-1]
    meiZiInMySQL = BlackStockingModel.query.order_by("id DESC").limit(30)

    for mz in blackStockingMeiZi:
        flag = 0
        for bcm in meiZiInMySQL:
            if bcm.imgsrc == mz["imgsrc"]:
                flag = 1
                break;
        if flag == 0:
            mmzz = BlackStockingModel(mz["imgsrc"], mz["title"], mz["topiclink"], mz["startcount"])
            db.session.add(mmzz)
            try:
                db.session.commit()
            except:
                db.session.rollback()

    return "update blackStockingMeiZi SUCCESS"


'''
    定时更新美腿妹
'''
@app.route('/updateCharmingLegs')
def updateCharmingLegs():
    charmingLegsMeiZi = MeiZiSpider().getMeiZiAtPage(1, 3)[::-1]
    meiZiInMySQL = CharmingLegsModel.query.order_by("id DESC").limit(30)

    for mz in charmingLegsMeiZi:
        flag = 0
        for bcm in meiZiInMySQL:
            if bcm.imgsrc == mz["imgsrc"]:
                flag = 1
                break;
        if flag == 0:
            mmzz = CharmingLegsModel(mz["imgsrc"], mz["title"], mz["topiclink"], mz["startcount"])
            db.session.add(mmzz)
            try:
                db.session.commit()
            except:
                db.session.rollback()
    return "update charmingLegsMeiZi SUCCESS"
            
'''
    定时更新大杂烩
'''
@app.route('/updateHodgepodge')
def updateHodgepodgeMeiZi():
    hodgepodgeMeiZi = MeiZiSpider().getMeiZiAtPage(1, 5)[::-1]
    meiZiInMySQL = HodgepodgeModel.query.order_by("id DESC").limit(30)

    for mz in hodgepodgeMeiZi:
        flag = 0
        for bcm in meiZiInMySQL:
            if bcm.imgsrc == mz["imgsrc"]:
                flag = 1
                break;
        if flag == 0:
            mmzz = HodgepodgeModel(mz["imgsrc"], mz["title"], mz["topiclink"], mz["startcount"])
            db.session.add(mmzz)
            try:
                db.session.commit()
            except:
                db.session.rollback()
	
    return "update hodgepodgeMeiZi SUCCESS"
            
'''
    定时更新妹子
'''
@app.route('/updateMeiZi')
def updateMeiZi():
    meiZi = MeiZiSpider().getMeiZiAtPage(2, 1)[::-1]
    meiZi = meiZi + MeiZiSpider().getMeiZiAtPage(1, 1)[::-1]
    meiZiInMySQL = MeiZiModel.query.order_by("id DESC").limit(60)
    
    for mz in meiZi:
        flag = 0
        for bcm in meiZiInMySQL:
            if bcm.imgsrc == mz["imgsrc"]:
                flag = 1
                break;
        if flag == 0:
            mmzz = MeiZiModel(mz["imgsrc"], mz["title"], mz["topiclink"], mz["startcount"])
            db.session.add(mmzz)
            try:
                db.session.commit()
            except:
                db.session.rollback()
	
    return "update meizi success"
    
    '''
    flag = 0
    for bcm in meiZi:
        if bcm["imgsrc"] != meiZiInMySQL.imgsrc and flag == 0:
            continue
        elif bcm["imgsrc"] == meiZiInMySQL.imgsrc and flag == 0:
            flag = 1
            continue
        else:
            mz = MeiZiModel(bcm["imgsrc"], bcm["title"], bcm["topiclink"], bcm["startcount"])
            db.session.add(mz)
            try:
                db.session.commit()
            except:
                db.session.rollback()
    return "update meiZi SUCCESS"
    '''        

'''
    定时更新小翘臀
'''
@app.route('/updateSmallBottom')
def updateSmallBottomMeiZi():
    smallBottomMeiZi = MeiZiSpider().getMeiZiAtPage(1, 6)[::-1]
    meiZiInMySQL = SmallBottomModel.query.order_by("id DESC").limit(30)

    for mz in smallBottomMeiZi:
        flag = 0
        for bcm in meiZiInMySQL:
            if bcm.imgsrc == mz["imgsrc"]:
                flag = 1
                break;
        if flag == 0:
            mmzz = SmallBottomModel(mz["imgsrc"], mz["title"], mz["topiclink"], mz["startcount"])
            db.session.add(mmzz)
            try:
                db.session.commit()
            except:
                db.session.rollback()
    return "update smallBottomMeiZi SUCCESS"
            
'''
    定时更新小清新
'''
@app.route('/updateSmallFresh')
def updateSmallFresh():
    smallFreshMeiZi = MeiZiSpider().getMeiZiAtPage(1, 4)[::-1]
    meiZiInMySQL = SmallFreshModel.query.order_by("id DESC").limit(30)

    for mz in smallFreshMeiZi:
        flag = 0
        for bcm in meiZiInMySQL:
            if bcm.imgsrc == mz["imgsrc"]:
                flag = 1
                break;
        if flag == 0:
            mmzz = SmallFreshModel(mz["imgsrc"], mz["title"], mz["topiclink"], mz["startcount"])
            db.session.add(mmzz)
            try:
                db.session.commit()
            except:
                db.session.rollback()
	#return MeiZiSpider().getMeiZiAtPage(1, 4)
    return "update smallFreshMeiZi SUCCESS"


'''
    NAME:       getMeiziBySpider
    FUNCTION:   通过爬虫获取妹子
    PARAM:      page---页数，cid---类别，大胸妹or黑丝袜or小清新等等
    RETURN:     JSON
'''
@app.route('/getMeiZi/')
def getMeiziBySpider():
    if request.method == 'GET':
        page = int(request.args.get("page", 1))
        cid = int(request.args.get("cid", 1))
        mz = MeiZiSpider().getMeiZiAtPage(page, cid)
        return jsonify(meizi=mz)

'''
    NAME:       getMeiZi       
    FUNCTION:   获取妹子的信息, 通过数据库,这个方法是推荐的
    PARAM:      limit---多少张，offset---偏移，cid---类别
'''
@app.route('/meizi/', methods=['GET'])
def getMeiZi():
    if request.method == 'GET':
        lim = int(request.args.get('limit', 30))
        off = int(request.args.get('offset',0))
        cid = int(request.args.get('cid', 1))
        data = []
        if cid == 1:
            data = MeiZiModel.query.order_by('id DESC').limit(lim).offset(off)
        elif cid == 2:
            data = BigChestModel.query.order_by('id DESC').limit(lim).offset(off)
        elif cid == 3:
            data = CharmingLegsModel.query.order_by('id DESC').limit(lim).offset(off)
        elif cid == 4:
            data = SmallFreshModel.query.order_by('id DESC').limit(lim).offset(off)
        elif cid == 5:
            data = HodgepodgeModel.query.order_by('id DESC').limit(lim).offset(off)
        elif cid == 6:
            data = SmallBottomModel.query.order_by('id DESC').limit(lim).offset(off)
        elif cid == 7:
            data = BlackStockingModel.query.order_by('id DESC').limit(lim).offset(off)
        else:
            return jsonify(meizi="")
        return jsonify(meizi = [i.serialize for i in data]) 

@app.before_request
def before_request():
    db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS,
    MYSQL_DB, port=int(MYSQL_PORT))

@app.teardown_request
def teardown_request(exception):
    if app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']:
        if exception is None:
            try:
                db.session.commit()
            except:
                db.session.rollback()
    db.session.remove()
    return exception
