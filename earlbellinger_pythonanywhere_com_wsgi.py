# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.

import sys
import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# add your project directory to the sys.path
#project_home = '/home/earlbellinger/mysite'
project_home = '/home/earlbellinger/pythonanywhere'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from flask_hello import app as application  # noqa
