from google.appengine.ext import db

class Location(db.Model):
    longitude = db.FloatProperty(required=True)
    latitude = db.FloatProperty(required=True)


