# -*- coding: utf-8 -*-
"""
Auth* related model.

This is where the models used by :mod:`repoze.who` and :mod:`repoze.what` are
defined.

It's perfectly fine to re-use this definition in the hiringpond application,
though.

"""
import os
import simplejson
import sys

from datetime import datetime

try:
    from hashlib import sha256
except ImportError:
    sys.exit('ImportError: No module named hashlib\n'
             'If you are on python2.4 this library is not part of python. '
             'Please install it. Example: easy_install hashlib')

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime, LargeBinary
from sqlalchemy.orm import relation, synonym, relationship

from hiringpond.model import DeclarativeBase, metadata, DBSession

__all__ = ['User', 'Group', 'Permission']


#{ Association tables


# This is the association table for the many-to-many relationship between
# groups and permissions. This is required by repoze.what.
group_permission_table = Table('tg_group_permission', metadata,
    Column('group_id', Integer, ForeignKey('tg_group.group_id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('permission_id', Integer, ForeignKey('tg_permission.permission_id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)

# This is the association table for the many-to-many relationship between
# groups and members - this is, the memberships. It's required by repoze.what.
user_group_table = Table('tg_user_group', metadata,
    Column('user_id', Integer, ForeignKey('tg_user.user_id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('group_id', Integer, ForeignKey('tg_group.group_id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)


#{ The auth* model itself


class Group(DeclarativeBase):
    """
    Group definition for :mod:`repoze.what`.

    Only the ``group_name`` column is required by :mod:`repoze.what`.

    """

    __tablename__ = 'tg_group'

    #{ Columns

    group_id = Column(Integer, autoincrement=True, primary_key=True)

    group_name = Column(Unicode(16), unique=True, nullable=False)

    display_name = Column(Unicode(255))

    created = Column(DateTime, default=datetime.now)

    #{ Relations

    users = relation('User', secondary=user_group_table, backref='groups')

    #{ Special methods

    def __repr__(self):
        return ('<Group: name=%s>' % self.group_name).encode('utf-8')

    def __unicode__(self):
        return self.group_name

    #}


# The 'info' argument we're passing to the email_address and password columns
# contain metadata that Rum (http://python-rum.org/) can use generate an
# admin interface for your models.
class User(DeclarativeBase):
    """
    User definition.

    This is the user definition used by :mod:`repoze.who`, which requires at
    least the ``user_name`` column.

    In addition, we specify all the local user information that we
    will be storing.

    """
    __tablename__ = 'tg_user'

    ##{B:Columns}

    user_id = Column(Integer, autoincrement=True, primary_key=True)

    user_name = Column(Unicode(16), unique=True, nullable=False)

    email_address = Column(Unicode(1024), unique=True, nullable=False)

    display_name = Column(Unicode(255))

    title = Column(Unicode(64))

    streetaddress = Column(Unicode(255))

    city = Column(Unicode(255))

    state_province = Column(Unicode(255))

    postal_code = Column(Unicode(12))

    country = Column(Unicode(32))

    phones = Column(Unicode(1024)) # JSON Encoded

    logo = Column(LargeBinary(1024*256))

    callingcard = Column(LargeBinary(1024*256))

    photo = Column(LargeBinary(1024*256))

    external_links = Column(Unicode(1024*256)) # JSON Encoded

    default_summary = Column(Unicode(8192))

    analyticsid = Column(Unicode(32))

    _password = Column('password', Unicode(128),
                       info={'rum': {'field':'Password'}})

    created = Column(DateTime, default=datetime.now)

    jobs = relationship("JobHistory", backref="user", order_by="JobHistory.order")
    skillgroups = relationship("SkillGroups", backref="user", order_by="SkillGroups.order")
    projects = relationship("ProjectHistory", backref="user", order_by="ProjectHistory.order")
    education = relationship("Education", backref="user", order_by="Education.order")
    awards = relationship("Award", backref="user", order_by="Award.order")
    resumes = relationship("Resume", backref="user", order_by="Resume.name")

    ##{E:Columns}

    #{ Special methods

    def __repr__(self):
        return ('<User: name=%s, email=%s, display=%s>' % (
                self.user_name, self.email_address, self.display_name)).encode('utf-8')

    def __unicode__(self):
        return self.display_name or self.user_name

    #{ Getters and setters

    @property
    def permissions(self):
        """Return a set with all permissions granted to the user."""
        perms = set()
        for g in self.groups:
            perms = perms | set(g.permissions)
        return perms

    @classmethod
    def by_email_address(cls, email):
        """Return the user object whose email address is ``email``."""
        return DBSession.query(cls).filter_by(email_address=email).first()

    @classmethod
    def by_user_name(cls, username):
        """Return the user object whose user name is ``username``."""
        return DBSession.query(cls).filter_by(user_name=username).first()

    @classmethod
    def _hash_password(cls, password):
        # Make sure password is a str because we cannot hash unicode objects
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        salt = sha256()
        salt.update(os.urandom(60))
        hash = sha256()
        hash.update(password + salt.hexdigest())
        password = salt.hexdigest() + hash.hexdigest()
        # Make sure the hashed password is a unicode object at the end of the
        # process because SQLAlchemy _wants_ unicode objects for Unicode cols
        if not isinstance(password, unicode):
            password = password.decode('utf-8')
        return password

    def _set_password(self, password):
        """Hash ``password`` on the fly and store its hashed version."""
        self._password = self._hash_password(password)

    def _get_password(self):
        """Return the hashed version of the password."""
        return self._password

    password = synonym('_password', descriptor=property(_get_password,
                                                        _set_password))

    #}

    def validate_password(self, password):
        """
        Check the password against existing credentials.

        :param password: the password that was provided by the user to
            try and authenticate. This is the clear text version that we will
            need to match against the hashed one in the database.
        :type password: unicode object.
        :return: Whether the password is valid.
        :rtype: bool

        """
        hash = sha256()
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        hash.update(password + str(self.password[:64]))
        return self.password[64:] == hash.hexdigest()

    def phones_to_string(self):
        phones = simplejson.loads(self.phones)
        return ", ".join(["%s: %s" % (x, phones[x]) for x in sorted(phones)])

    def phones_to_dict(self):
        return simplejson.loads(self.phones)
    
    def links_to_dict(self):
        return simplejson.loads(self.external_links)

class Permission(DeclarativeBase):
    """
    Permission definition for :mod:`repoze.what`.

    Only the ``permission_name`` column is required by :mod:`repoze.what`.

    """

    __tablename__ = 'tg_permission'

    #{ Columns

    permission_id = Column(Integer, autoincrement=True, primary_key=True)

    permission_name = Column(Unicode(63), unique=True, nullable=False)

    description = Column(Unicode(255))

    #{ Relations

    groups = relation(Group, secondary=group_permission_table,
                      backref='permissions')

    #{ Special methods

    def __repr__(self):
        return ('<Permission: name=%s>' % self.permission_name).encode('utf-8')

    def __unicode__(self):
        return self.permission_name

    #}


#}
