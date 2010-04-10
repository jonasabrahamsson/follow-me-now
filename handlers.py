import os
import logging
import uuid
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from django.utils import simplejson

import model

class AcquireId(webapp.RequestHandler):

    def get(self):
        self.response.out.write(simplejson.dumps(str(uuid.uuid4())))
    
class LocationHandler(webapp.RequestHandler):

    def get(self, id):
        logging.error(id)
        location = model.Location.get_by_key_name(id)
        if location is not None:
            return self.response.out.write(simplejson.dumps({'latitude':location.latitude, 
								'longitude':location.longitude}))
        return self.response.out.write(simplejson.dumps(()))


    def post(self, id):
        longitude = float(self.request.POST["longitude"])
        latitude = float(self.request.POST["latitude"])
        location = model.Location(key_name=id, longitude=longitude, latitude=latitude)
        location.put()
	#self.redirect('/%s/'%id)

class GpsHandler(webapp.RequestHandler):

  def get(self, id=None):
    template_values = {}
    path = os.path.join(os.path.dirname(__file__), 'gps.html')
    self.response.out.write(template.render(path, template_values))

  def post(self, id):
      longitude = float(self.request.POST["longitude"])
      latitude = float(self.request.POST["latitude"])
      location = model.Location(key_name=id, longitude=longitude, latitude=latitude)
      location.put()
      self.redirect('/%s/gps/' % id)

class DevHandler(webapp.RequestHandler):

  def get(self, id):
    location = model.Location.get_by_key_name(id)
    template_values = {'id':id, 'longitude':location.longitude, 'latitude':location.latitude}
    path = os.path.join(os.path.dirname(__file__), 'dev.html')
    self.response.out.write(template.render(path, template_values))

  def post(self, id):
      longitude = float(self.request.POST["longitude"])
      latitude = float(self.request.POST["latitude"])
      location = model.Location(key_name=id, longitude=longitude, latitude=latitude)
      location.put()
      self.redirect('/%s/dev/' % id)

class MainHandler(webapp.RequestHandler):

  def get(self, id):
    template_values = {'id':id}
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))
