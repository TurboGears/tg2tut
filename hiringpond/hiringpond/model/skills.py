# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DATE
from sqlalchemy.orm import relation, backref, relationship

from hiringpond.model import DeclarativeBase, metadata, DBSession


class SkillGroups(DeclarativeBase):
    __tablename__ = 'skill_groups'
    
    ##{B:Columns}
    
    id = Column(Integer, primary_key=True)
    
    order = Column(Integer)    
    name = Column(Unicode(64))
    tags = Column(Unicode(1024))
    
    userid = Column(Integer, ForeignKey('tg_user.user_id'))
    skills = relationship("SpecificSkills", backref="skillgroups")
    
    ##{E:Columns}

class SpecificSkills(DeclarativeBase):
    __tablename__ = 'specific_skills'

    ##{B:Columns}

    id = Column(Integer, primary_key=True)
    
    order = Column(Integer)    
    name = Column(Unicode(64))
    time_used = Column(Unicode(16))
    last_used = Column(DATE())
    proficiency = Column(Unicode(10))
    tags = Column(Unicode(1024))
    
    skillgroupid = Column(Integer, ForeignKey('skill_groups.id'))
    
    ##{E:Columns}
