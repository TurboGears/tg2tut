# -*- coding: utf-8 -*-

"""The base Controller API."""

from tg import TGController, tmpl_context, config
from tg.render import render
from tg import request
from tg.i18n import ugettext as _, ungettext

import hiringpond.model as model
from hiringpond.lib.util import rst_to_html

__all__ = ['BaseController']


class BaseController(TGController):
    """
    Base class for the controllers in the application.

    Your web application should have one of these. The root of
    your application is used to compute URLs used by your app.

    """

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # TGController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']

        request.identity = request.environ.get('repoze.who.identity')
        tmpl_context.identity = request.identity
        tmpl_context.rst_to_html = rst_to_html
        tmpl_context.gaid = config.get('ga_verifier', None)
        tmpl_context.analyticsid = config.get('analyticsid', None)
        return TGController.__call__(self, environ, start_response)
