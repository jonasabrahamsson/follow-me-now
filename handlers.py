import logging
import uuid
from google.appengine.ext import webapp
from django.utils import simplejson

import model

class AquireId(webapp.RequestHandler):

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
        longitude = float(self.request.GET["longitude"])
        latitude = float(self.request.GET["latitude"])
        location = model.Location(key_name=id, longitude=longitude, latitude=latitude)
        location.put()
