# -*- coding: utf-8 -*-

from hiringpond.model import DBSession, User

def get_user_or_default_user(uid=None):
    if not uid:
        user = DBSession.query(User).filter(User.email_address=='wilee@example.com').first()
    else:
        try:
            user = DBSession.query(User).filter(User.user_id==uid).first()
        except:
            user = DBSession.query(User).filter(User.email_address=='wilee@example.com').first()
    if not user:
        user = DBSession.query(User).filter(User.email_address=='wilee@example.com').first()
    return user
