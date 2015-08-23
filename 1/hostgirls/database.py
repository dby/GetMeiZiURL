#coding=utf-8

from flaskext.sqlalchemy import SQLAlchemy 

import MySQLdb
from . import app

class nullpool_SQLAlchemy(SQLAlchemy): 
    def apply_driver_hacks(self, app, info, options): 
        super(nullpool_SQLAlchemy, self).apply_driver_hacks(app, info, options) 
        from sqlalchemy.pool import NullPool 
        options['poolclass'] = NullPool 
        del options['pool_size']

db = nullpool_SQLAlchemy(app)
#db = SQLAlchemy(app)

