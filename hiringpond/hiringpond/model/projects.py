# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DATE, Boolean
from sqlalchemy.orm import relation, backref, relationship

from hiringpond.model import DeclarativeBase, metadata, DBSession


class ProjectHistory(DeclarativeBase):
    __tablename__ = 'project_history'
    
    ##{B:Columns}
    
    id = Column(Integer, primary_key=True)
    
    order = Column(Integer)
    name = Column(Unicode(64))
    summary = Column(Unicode(4096))
    start = Column(DATE())
    end = Column(DATE())
    tools_used = Column(Unicode(128))
    tags = Column(Unicode(1024))
    hidden = Column(Boolean())
    
    userid = Column(Integer, ForeignKey('tg_user.user_id'))
    companyid = Column(Integer, ForeignKey('job_history.id'))
    project_bullets = relationship("ProjectPoints", backref="project")
    
    ##{E:Columns}

class ProjectPoints(DeclarativeBase):
    __tablename__ = 'project_points'
    
    ##{B:Columns}
    
    id = Column(Integer, primary_key=True)
    
    order = Column(Integer)
    bullet_text = Column(Unicode(1024))
    tags = Column(Unicode(1024))
    hidden = Column(Boolean())
     
    projectid = Column(Integer, ForeignKey('project_history.id'))
    
    ##{E:Columns}

