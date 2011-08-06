# -*- coding: utf-8 -*-
"""Setup the Wiki-20 application"""

import logging
import transaction
from tg import config

def setup_schema(command, conf, vars):
    """Place any commands to setup wiki20 here"""
    # Load the models

    # <websetup.websetup.schema.before.model.import>
    from wiki20 import model
    # <websetup.websetup.schema.after.model.import>

    
    # <websetup.websetup.schema.before.metadata.create_all>
    print "Creating tables"
    model.metadata.create_all(bind=config['pylons.app_globals'].sa_engine)
    # <websetup.websetup.schema.after.metadata.create_all>
    transaction.commit()
    from migrate.versioning.shell import main
    main(argv=['version_control'], url=config['sqlalchemy.url'], repository='migration', name='migration')
