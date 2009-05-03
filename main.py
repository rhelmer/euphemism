import cgi
import os

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class Container(db.Model):
  dom_id = db.StringProperty()
  date = db.DateTimeProperty(auto_now_add=True)
  top = db.StringProperty()
  left = db.StringProperty()
  width = db.StringProperty()
  height = db.StringProperty()

class Content(db.Model):
  dom_id = db.StringProperty()
  text = db.StringProperty()
  date = db.DateTimeProperty(auto_now_add=True)

class Save(webapp.RequestHandler):
  def post(self):
    container = Container()
    container.dom_id = self.request.get('id')
    container.top = self.request.get('top')
    container.left = self.request.get('left')
    container.width = self.request.get('width')
    container.height = self.request.get('height')
    container.put()

    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write(container.dom_id)

class SaveContent(webapp.RequestHandler):
  def post(self):
    content = Content()
    content.text = self.request.get('text')
    content.dom_id = self.request.get('id')
    content.put()

    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write(content.text);

class MainPage(webapp.RequestHandler):
  def get(self):

    p_top = '0px';
    p_left = '0px';
    p_width = '';
    p_height = '';
    c_top = '0px';
    c_left = '0px';
    c_width = '';
    c_height = '';
    p = Container.gql("WHERE dom_id='post' ORDER BY date DESC LIMIT 1").get()
    c = Container.gql("WHERE dom_id='comments' ORDER BY date DESC LIMIT 1").get()
    if  p != None:
      p_top = p.top
      p_left = p.left
      p_width = p.width
      p_height = p.height
    if  c != None:
      c_top = c.top
      c_left = c.left
      c_width = c.width
      c_height = c.height

    post = Content.gql("WHERE dom_id='p1' ORDER BY date DESC LIMIT 1").get()
    comment1 = Content.gql("WHERE dom_id='c1' ORDER BY date DESC LIMIT 1").get()
    comment2 = Content.gql("WHERE dom_id='c2' ORDER BY date DESC LIMIT 1").get()

    if post == None:
      post = 'This is the post'
    if comment1 == None:
      comment1 = 'This is comment1'
    if comment2 == None:
      comment2 = 'This is comment2'

    template_values = {
      'post': post.text,
      'comment1': comment1.text,
      'comment2': comment2.text,
      'c_top': c_top,
      'c_left': c_left,
      'c_width': c_width,
      'c_height': c_height,
      'p_top': p_top,
      'p_left': p_left,
      'p_width': p_width,
      'p_height': p_height,
      'history': Container.all().order('-date').fetch(10)
    }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))


def main():
  application = webapp.WSGIApplication(
    [ 
      ('/', MainPage), 
      ('/save', Save),
      ('/save/content', SaveContent),
    ], debug=True)
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
