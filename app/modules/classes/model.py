from app import db
from datetime import datetime as dt

from app.modules.auth.model import User
from app.modules.events.model import Event

from wtforms import Form, validators, StringField, RadioField, \
    SelectMultipleField, DateTimeField

class Class(db.Document):
    owner = db.ReferenceField(User, required=True)
    name = db.StringField(required=True, min_length=3, max_length=50)
    professor = db.ReferenceField(User, required=True)
    events = db.ListField(db.ReferenceField(Event))
    start_time = db.DateTimeField(default=dt.now())
    end_time = db.DateTimeField(default=dt.now())
    days = db.ListField(db.StringField(default="",required=True))
    start_date = db.DateTimeField(default=dt.now())
    end_date = db.DateTimeField(default=dt.now())
    gcal_events = db.ListField(db.StringField(default=""))
    meta = {'strict': False}
