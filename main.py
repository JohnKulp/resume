
import os
import webapp2
import jinja2

from google.appengine.api import mail
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


class ResumeHandler(webapp2.RequestHandler):
  def get(self):
    pass
    #name="John Kulp Resume.docx"   
    #self.response.headers.add_header('Method','get')
    #self.response.headers.add_header('Content-Type','application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    #self.response.headers.add_header('name',name)
    #self.response.headers.add_header('Content-Disposition','attachment')
    #self.response.headers.add_header('filename',name)
    #self.response.headers.add_header('Content',text)
    #self.response.out.write(text)

class skill():
  def __init__(self, name, val):
    self.name = name
    self.val = val

class experience():
  def __init__(self, name, start_date, end_date, title, description):
    self.name = name
    self.start_date = start_date
    self.end_date = end_date
    self.title = title
    self.description = description

class MainPageHandler(webapp2.RequestHandler):
  def get(self):



    job_history = [
      experience(
          name="McKesson Pharmacy Solutions and Automation, Moon, PA",
          title="Software Development Intern",
          description="Developed a web-based QA metric aggregation application using the API for the issue-tracker JIRA.  It was used by management team to track EscapeRate and Deployment metrics.  The tools used were Node.js and JQuery.",
          start_date="June, 2015",
          end_date="August, 2015"
        ),
      experience(
          name="McKesson Pharmacy Solutions and Automation, Moon, PA",
          title="Software Development Intern",
          description="Developed a web-based consumer portal interface for an enterprise software suite through a SOAP XML API.  The tools used were Ruby on Rails and JQuery.",
          start_date="June, 2014",
          end_date="August, 2014"
        )
    ]
    education = [
      experience(
          name="University of Pittsburgh, Pittsburgh, PA",
          title="Bachelor of Science in Computer Science, Bachelor of Arts in Japanese",
          description="Current GPA 3.25.  Courses included: Data Structures, Operating Systems, Software Testing, Algorithm Implementation, Systems Software, and Web Development.",
          start_date="September, 2012",
          end_date="May, 2016"
        ),
      experience(
          name="Konan University, Kobe, Japan",
          title="Intensive Japanese Program",
          description="Cultural immersion - lived with a Japanese family.",
          start_date="September, 2014",
          end_date="May, 2015"
        )
    ]

    skills = [

      skill(name="Programming Languages", val=[

        skill(name="Java", val="90"),
        skill(name="C", val="70"),
        skill(name="Python", val="80"),
        skill(name="Javascript", val="70")
      ]),

      skill(name="Web Frameworks", val=[

        skill(name="Node.js", val="85"),
        skill(name="Google App Engine", val="60"),
        skill(name="Ruby on Rails", val="40")
      ]),

      skill(name="Services and Tools", val=[

        skill(name="Git", val="75"),
        skill(name="SOAP XML", val="50")
      ]),

      skill(name="Personal Skills", val=[

        skill(name="Public Speaking", val="95"),
        skill(name="Language Acquisition", val="90")
      ])
    ]

    languages = [ 
      skill(name = "English", val="100"),
      skill(name = "Japanese", val="80")
    ]


    params = {
      'education': education,
      'employment': job_history,
      'skills': skills,
      'languages': languages
    }

    uastring = self.request.headers.get('user_agent')

    if "Mobile" in uastring:
      render_template(self, 'mobile_index.html', params)
    else:
      render_template(self, 'index.html', params)


class MailHandler(webapp2.RequestHandler):
  def post(self):
    user_address = self.request.get("email-address")
    email_content = self.request.get("email-content")

    sender_address = "John Kulp <john.h.kulp@gmail.com>"
    subject = "New resume website message!"
    body = user_address + ": \n\n" + email_content
    mail.send_mail('john-kulp@john-kulp-resume.appspotmail.com', sender_address, subject, body)
    self.response.write("OK")

mappings = [
  ('/', MainPageHandler),
  ('/resume', ResumeHandler),
  ('/mail', MailHandler)
]
app = webapp2.WSGIApplication(mappings, debug=True)