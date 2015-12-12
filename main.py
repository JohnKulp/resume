
import os
import webapp2
import jinja2


from google.appengine.ext.webapp import template

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# We'll just use this convenience function to retrieve and render a template.
def render_template(handler, templatename, templatevalues={}):
  path = os.path.join(os.path.dirname(__file__), 'templates/' + templatename)
  html = template.render(path, templatevalues)
  handler.response.out.write(html)


class skill():
  def __init__(self, name, val):
    self.name = name
    self.val = val

class MainPageHandler(webapp2.RequestHandler):
  def get(self):


    languages = { 
      skill(name = "English", val="100"),
      skill(name = "Japanese", val="80")
    }

    skills = {

      skill(name="Programming Languages", val={

        skill(name="Java", val="90"),
        skill(name="C", val="70"),
        skill(name="Python", val="80"),
        skill(name="Javascript", val="70")
      }),

      skill(name="Web Frameworks", val={

        skill(name="Node.js", val="85"),
        skill(name="Google App Engine", val="60"),
        skill(name="Ruby on Rails", val="40")
      }),

      skill(name="Services and Tools", val={
        
        skill(name="Git", val="75"),
        skill(name="SOAP XML", val="50")
      })
    }



    params = {
      'education': '',
      'employment': '',
      'skills': skills,
      'languages': languages
    }

    render_template(self, 'index.html', params)

mappings = [
  ('/', MainPageHandler)
]
app = webapp2.WSGIApplication(mappings, debug=True)