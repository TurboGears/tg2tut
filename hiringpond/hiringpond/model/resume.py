# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from hiringpond.model import DeclarativeBase, metadata, DBSession


class Resume(DeclarativeBase):
    __tablename__ = 'resume'
    
    ##{B:Columns}
    
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128))
    
    includetags = Column(Unicode(1024))
    excludetags = Column(Unicode(1024))
    includesections = Column(Unicode(1024))
    excludesubsections = Column(Unicode(1024))
    excludebullets = Column(Unicode(4096))
    includebullets = Column(Unicode(1024))

    userid = Column(Integer, ForeignKey('tg_user.user_id'))

    ##{E:Columns}
