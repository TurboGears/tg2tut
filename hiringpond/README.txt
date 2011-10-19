This file is for you to describe the hiringpond application. Typically
you would include information such as the information below:

Installation and Setup
======================

Install ``hiringpond`` using the setup.py script::

    $ cd hiringpond
    $ python setup.py install

Create the project database for any model classes defined::

    $ paster setup-app development.ini

Start the paste http server::

    $ paster serve development.ini

While developing you may want the server to reload after changes in package files (or its dependencies) are saved. This can be achieved easily by adding the --reload option::

    $ paster serve --reload development.ini

Then you are ready to go.

TODO List
=========

 * add docutils to output strings where appropriate (everywhere?)
 * add login
 * add ability to edit own resume
 * add ability to compile new custom resumes
 * add ability to output PDF
 * add ability to output ODT
 * add ability to output DOC
 * add generic logo
 * add generic photo / head (shadow) shot
 * add ability to login using Google, Yahoo, Facebook, etc
 * add ability to send resumes directly from Hiring Pond
 * add ability to track where resumes have gone
 * add ability to track job hunt progress
 * add ability to track stats on resume sending
 * add ability to display current employment status (employed, unemployed, contracting)
 * add ability to display current employment seeking status (not at all, active, passive)
 * add logo to qrcode
 * change colors of qrcode
 * change color scheme for all of hiring pond to sunset and water
 * add fisherman silhouette as hiring pond logo
 * add privacy controls and honor them properly
 * complete tag support
 * add cover letter support
 * keywords metadata
 * description metadata
 * spell checker
 * add ability to parse incoming resume from .DOC/.PDF/.ODT
 * proper support for googlebot
 * support for myresume.hiringpond.com
 * add support for searching the whole site
 * add notice disclaiming trademark ownership
