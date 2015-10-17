import datetime
import logging
import os
import webapp2

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

###############################################################################
# We'll just use this convenience function to retrieve and render a template.
def render_template(handler, templatename, templatevalues={}):
  path = os.path.join(os.path.dirname(__file__), 'templates/' + templatename)
  html = template.render(path, templatevalues)
  handler.response.out.write(html)


###############################################################################
# We'll use this convenience function to retrieve the current user's email.
def get_user_email():
  result = None
  user = users.get_current_user()
  if user:
    result = user.email()
  return result

def get_profiles():
  result = list()
  q = PostedProfile.query()
  q = q.order(-PostedProfile.time_created)
  for prof in q.fetch(100):
    result.append(prof)
  return result


###############################################################################
class MainPageHandler(webapp2.RequestHandler):
  def get(self):
    profiles = get_profiles()
    email = get_user_email()
    page_params = {
      'profiles': profiles,
      'user_email': email,
      'login_url': users.create_login_url(),
      'logout_url': users.create_logout_url('/')
    }
    render_template(self, 'index.html', page_params)


###############################################################################
class CatPageHandler(webapp2.RequestHandler):
  def get(self):
    email = get_user_email()
    if email:
      page_params = {
        'user_email': email,
        'login_url': users.create_login_url(),
        'logout_url': users.create_logout_url('/')
      }
      render_template(self, 'cat.html', page_params)
    else:
      self.redirect('/')


###############################################################################
class PostedProfile(ndb.Model):
  uname = ndb.StringProperty()
  #profile_url = ndb.StringProperty()
  hobbies = ndb.StringProperty()
  interests= ndb.StringProperty()
  time_created = ndb.DateTimeProperty(auto_now_add=True)


mappings = [
  ('/', MainPageHandler),
  ('/cat', CatPageHandler)
]
app = webapp2.WSGIApplication(mappings, debug=True)x`