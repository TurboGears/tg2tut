# -*- coding: utf-8 -*-

from docutils.core import publish_parts

from tg import config

from hiringpond.model import DBSession, User

def get_user_or_default_user(uid=None):
    email = config.get('default_user_email', 'wilee@example.com')
    if not uid:
        user = DBSession.query(User).filter(User.email_address==email).first()
    else:
        try:
            user = DBSession.query(User).filter(User.user_id==uid).first()
        except:
            user = DBSession.query(User).filter(User.email_address==email).first()
    if not user:
        user = DBSession.query(User).filter(User.email_address==email).first()
    return user

def rst_to_html(fragment=''):
    if fragment is None:
        fragment = ''

    return publish_parts(fragment, writer_name='html')['fragment']
