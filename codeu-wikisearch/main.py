#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users
from jinja2 import Environment, PackageLoader
import webapp2
import jinja2
import os
import time
# class LoginHandler(webapp2.RequestHandler):
#     def get(self):
#         user = users.get_current_user()
#         if user:
#             greeting = ('Welcome, %s! (<a href = %s>sign_out</a>)' %
#             (user.nickname(), users.create_logout_url('/')))
#         else:
#             greeting = ('<a href ="%s">Sign in or register</a>.'%
#             users.create_login_url('/login'))
#         self.response.write('<html><body>%s</body></html>' % greeting)
JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape = True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        entry = JINJA_ENVIRONMENT.get_template('templates/entry.html')
        self.response.write(entry.render())

class ResultHandler(webapp2.RequestHandler):
    def get(self):
        page= JINJA_ENVIRONMENT.get_template('templates/results.html')
        self.response.write(page.render())




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultHandler)
], debug=True)
