# -*- coding: utf-8 -*-
"""
Global configuration file for TG2-specific settings in hiringpond.

This file complements development/deployment.ini.

Please note that **all the argument values are strings**. If you want to
convert them into boolean, for example, you should use the
:func:`paste.deploy.converters.asbool` function, as in::
    
    from paste.deploy.converters import asbool
    setting = asbool(global_conf.get('the_setting'))
 
"""

from tg.configuration import AppConfig, config
#from tg.render import my_pylons_globals

from genshi.template import TemplateLoader, NewTextTemplate
from pylons import (app_globals, session, tmpl_context, request,
                    response, templating)

import hiringpond
from hiringpond import model
from hiringpond.lib import app_globals, helpers 

class VCardTemplateLoader(TemplateLoader):
    template_extension = '.vcf'

    def get_dotted_filename(self, filename):
        if not filename.endswith(self.template_extension):
            finder = config['pylons.app_globals'].dotted_filename_finder
            filename = finder.get_dotted_filename(
                    template_name=filename,
                    template_extension=self.template_extension)
        return filename

    def load(self, filename, relative_to=None, cls=None, encoding=None):
        """Actual loader function."""
        return TemplateLoader.load(
                self, self.get_dotted_filename(filename),
                relative_to=relative_to, cls=NewTextTemplate, encoding=encoding)

class RenderVCard(object):
    """Singleton that can be called as the vcard render function."""

    genshi_functions = {} # auxiliary Genshi functions loaded on demand

    def __init__(self, loader):
        if not self.genshi_functions:
            from genshi import HTML, XML
            self.genshi_functions.update(HTML=HTML, XML=XML)
        self.load_template = loader.load

    def __call__(self, template_name, template_vars, **kwargs):
        """Render the template_vars with the Genshi template."""
        template_vars.update(self.genshi_functions)

        # Gets document type from content type or from config options
        doctype = 'text/x-vcard'
        method='vcf'
        kwargs['doctype'] = doctype
        kwargs['method'] = method

        def render_template():
            #template_vars.update(my_pylons_globals())
            template = self.load_template(template_name)
            return template.generate(**template_vars).render(encoding=None)

        return templating.cached_template(
            template_name, render_template,
            **kwargs)


class HiringPondConfig(AppConfig):
    def setup_vcard_renderer(self):
        loader = VCardTemplateLoader(search_path=self.paths.templates,
                                auto_reload=self.auto_reload_templates)

        print loader.get_dotted_filename('hiringpond.templates.vcard')
        self.render_functions.vcard = RenderVCard(loader)


base_config = HiringPondConfig()
base_config.renderers = []

base_config.package = hiringpond

#Enable json in expose
base_config.renderers.append('json')
#Set the default renderer
base_config.default_renderer = 'genshi'
base_config.renderers.append('genshi')
# Add vcard rendering (genshi plain text renderer)
base_config.renderers.append('vcard')

# if you want raw speed and have installed chameleon.genshi
# you should try to use this renderer instead.
# warning: for the moment chameleon does not handle i18n translations
#base_config.renderers.append('chameleon_genshi')
#Configure the base SQLALchemy Setup
base_config.use_sqlalchemy = True
base_config.model = hiringpond.model
base_config.DBSession = hiringpond.model.DBSession
# Configure the authentication backend

# YOU MUST CHANGE THIS VALUE IN PRODUCTION TO SECURE YOUR APP 
base_config.sa_auth.cookie_secret = "ChangeME" 

base_config.auth_backend = 'sqlalchemy'
base_config.sa_auth.dbsession = model.DBSession
# what is the class you want to use to search for users in the database
base_config.sa_auth.user_class = model.User
# what is the class you want to use to search for groups in the database
base_config.sa_auth.group_class = model.Group
# what is the class you want to use to search for permissions in the database
base_config.sa_auth.permission_class = model.Permission

# override this if you would like to provide a different who plugin for
# managing login and logout of your application
base_config.sa_auth.form_plugin = None

# override this if you are using a different charset for the login form
base_config.sa_auth.charset = 'utf-8'

# You may optionally define a page where you want users to be redirected to
# on login:
base_config.sa_auth.post_login_url = '/post_login'

# You may optionally define a page where you want users to be redirected to
# on logout:
base_config.sa_auth.post_logout_url = '/post_logout'
