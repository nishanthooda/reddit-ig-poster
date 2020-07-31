from peewee import *
import datetime

db = SqliteDatabase('reddit-ig-poster.db')

class BaseModel(Model):
  class Meta:
      database = db

class Post(BaseModel):
  reddit_id = CharField(unique=True)
  saved_at = DateTimeField(default=datetime.datetime.now)
  image_url = TextField()
  subreddit = CharField()
  rating = FloatField()

db.connect()
db.create_tables([Post])