# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DATE
from sqlalchemy.orm import relation, backref, relationship

from hiringpond.model import DeclarativeBase, metadata, DBSession


class Education(DeclarativeBase):
    __tablename__ = 'education'
    
    ##{B:Columns}
    
    id = Column(Integer, primary_key=True)
    education = Column(Unicode(255))
    date_completed = Column(DATE())
    userid = Column(Integer, ForeignKey('tg_user.user_id'))
    
    ##{E:Columns}

class Award(DeclarativeBase):
    __tablename__ = 'awards'

    ##{B:Columns}
    
    id = Column(Integer, primary_key=True)
    award = Column(Unicode(255))
    date_awarded = Column(DATE())
    userid = Column(Integer, ForeignKey('tg_user.user_id'))
    
    ##{E:Columns}

