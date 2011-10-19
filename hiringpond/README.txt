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

 * add login
 * add ability to edit own resume
 * complete tag support
 * add ability to define the default user, and make it the only thing that displays (i.e.: single posted resume mode)
 * add ability to compile new custom resumes
 * add ability to change default resume displayed
 * add ability to output PDF
 * add ability to output ODT
 * add ability to output DOC
 * add ability to output EPUB
 * add ability to allow user to post unredacted publicly downloadable resumes on their page
 * add privacy controls and honor them properly
 * add ability to display current employment status (employed, unemployed, contracting)
 * add ability to display current employment seeking status (not at all, active, passive)
 * change color scheme for all of hiring pond to sunset and water
 * add fisherman silhouette as hiring pond logo
 * add generic logo
 * add generic photo / head (shadow) shot
 * add ability to register new account
 * add ability to change default user
 * add ability to delete user
 * add ability to suspend/hide user
 * add ability to login using Google, Yahoo, Facebook, etc
 * add cover letter support
 * add ability to send resumes directly from Hiring Pond
 * add ability to track where resumes have gone
 * add ability to track job hunt progress
 * add ability to track stats on resume sending
 * add support for searching the whole site
 * add support for adding in a google-analytics account per resume
 * add support for adding in a google-analytics account for all site
 * add support for adding in a google verifier meta tag for all site
 * add logo to qrcode
 * change colors of qrcode
 * spell checker
 * proper support for googlebot
 * support for myresume.hiringpond.com and www.hiringpond.com/myresume
 * add support for contracting companies to be able to advertise their available staff
 * add storage quotas/limits
 * add support for requesting an un-redacted version of a user's resume
 * add support for responding to resume requests
 * add support for sending resumes using json, soap, xmlrpc
 * add support for uploading to Monster, Dice, Indeed, etc
 * add template support to allow different layouts of HTML and printed resumes
 * add ability to update linkedin status when adding a bullet point
 * add ability to parse incoming resume from .DOC/.PDF/.ODT
