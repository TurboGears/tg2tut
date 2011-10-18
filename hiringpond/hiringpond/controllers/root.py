# -*- coding: utf-8 -*-
"""Main Controller"""

from datetime import datetime
from StringIO import StringIO

from tg import expose, flash, require, url, request, redirect, render
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tgext.admin.tgadminconfig import TGAdminConfig
from repoze.what import predicates

from hiringpond.lib.base import BaseController
from hiringpond.lib.util import get_user_or_default_user
from hiringpond.lib import pyqrcode
from hiringpond.model import DBSession, metadata, User
from hiringpond import model

from hiringpond.controllers.error import ErrorController

__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the hiringpond application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    error = ErrorController()

    @expose('hiringpond.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('hiringpond.templates.resume')
    def resume(self, uid=None, fmt='html', tags=''):
        user = get_user_or_default_user(uid)
        return {'user': user, 'tags': set(tags.split(','))}
    
    @expose()
    def photo(self, uid=None):
        user = get_user_or_default_user(uid)
        return user.photo
    
    @expose()
    def logo(self, uid=None):
        user = get_user_or_default_user(uid)
        return user.logo

    @expose(content_type='image/png')
    def vcard(self, uid=None):
        user = get_user_or_default_user(uid)
        data = pyqrcode.MakeQRImage(render.render({'user':user}, template_engine='vcard', template_name='hiringpond.templates.vcard'))
        buff = StringIO()
        data.save(buff, 'png')
        img = buff.getvalue()
        buff.close()
        return img

    @expose('vcard:hiringpond.templates.vcard', content_type='text/x-vcard')
    def vcf(self, uid=None):
        user = get_user_or_default_user(uid)
        return {'user':user}
    
    @expose('hiringpond.templates.login')
    def login(self, came_from=url('/')):
        """Start the user login."""
        login_counter = request.environ['repoze.who.logins']
        if login_counter > 0:
            flash(_('Wrong credentials'), 'warning')
        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from)

    @expose()
    def post_login(self, came_from='/'):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ['repoze.who.logins'] + 1
            redirect('/login',
                params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)
        redirect(came_from)

    @expose()
    def post_logout(self, came_from=url('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        redirect(came_from)
