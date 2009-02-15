import cgi
import os

from google.appengine.api import urlfetch
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import memcache

class Weather(webapp.RequestHandler):
  def get(self):
    content = memcache.get('94530')
    if content is None:
      url = 'http://xml.customweather.com/xml?zip_code=94530&client=alex&client_password=trust_me&product=current_conditions'
      try:
        result = urlfetch.fetch(url, headers={'Accept-encoding': 'gzip'})
        content = result.content
        if result.status_code == 200:
          memcache.add('94530', content, 10)
      except:
        return
    self.response.headers['Content-Type'] = 'text/xml'
    self.response.out.write(content)

class MainPage(webapp.RequestHandler):
  def get(self):
    template_values = {}

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/weather', Weather)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
