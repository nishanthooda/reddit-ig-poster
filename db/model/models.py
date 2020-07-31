from peewee import *

db = SqliteDatabase('reddit-ig-poster.db')

class Post(Model):
    reddit_name = TextField()
    image_url = TextField()
    subreddit = TextField

    class Meta:
        database = db # This model uses the "people.db" database.