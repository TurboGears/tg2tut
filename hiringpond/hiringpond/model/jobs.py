# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DATE, Boolean
from sqlalchemy.orm import relation, backref, relationship

from hiringpond.model import DeclarativeBase, metadata, DBSession


class JobHistory(DeclarativeBase):
    __tablename__ = 'job_history'
    
    ##{B:Columns}
    
    id = Column(Integer, primary_key=True)
    
    order = Column(Integer)
    company_name = Column(Unicode(64))
    job_title = Column(Unicode(64))
    job_city = Column(Unicode(64))
    job_state = Column(Unicode(48))
    start_date = Column(DATE())
    end_date = Column(DATE())
    job_summary = Column(Unicode(4096))
    tags = Column(Unicode(1024))
    hidden = Column(Boolean())
    
    userid = Column(Integer, ForeignKey('tg_user.user_id'))
    job_bullets = relationship("JobPoints", backref="job", order_by="JobPoints.order")
    projects = relationship("ProjectHistory", backref="job")
    
    ##{E:Columns}

class JobPoints(DeclarativeBase):
    __tablename__ = 'job_bullet_points'
    
    ##{B:Columns}
    
    id = Column(Integer, primary_key=True)
    
    order = Column(Integer)    
    bullet_text = Column(Unicode(1024))
    tags = Column(Unicode(1024))
    hidden = Column(Boolean())
    
    jobid = Column(Integer, ForeignKey('job_history.id'))
    
    ##{E:Columns}

