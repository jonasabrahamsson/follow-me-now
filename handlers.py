import logging
from google.appengine.ext import webapp
from django.utils import simplejson
import model

class UpdateLocation(webapp.RequestHandler):

    def get(self):
        id = self.request.GET["id"]
        longitude = float(self.request.GET["longitude"])
        latitude = float(self.request.GET["latitude"])
        location = model.Location(key_name=id, longitude=longitude, latitude=latitude)
        location.put()


class GetLocation(webapp.RequestHandler):

    def get(self):
        id = self.request.GET["id"]
        logging.error(id)
        location = model.Location.get_by_key_name(id)
        if location is not None:
            return self.response.out.write(simplejson.dumps({'latitude':location.latitude, 
								'longitude':location.longitude}))
        return self.response.out.write(simplejson.dumps(()))
