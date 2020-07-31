import requests
import json
import urllib.request
import sqlite3
from peewee import *
import datetime
import pdb
from db.create_database import Post
import os

class PullReddit:
  def __init__(self, subreddit):
    self.subreddit = subreddit

  def get_top_historic_data(self, length):
    url = "https://api.reddit.com/r/" + self.subreddit + "/top?t=" + length + "&limit=100"
    response = requests.get(url, headers={'Content-Type': 'application/json', 'User-agent': 'nishant-mac'})
    posts = response.json()['data']['children']
    return posts

  def is_quality_post(self, post):
    if post['data']['ups'] > 10000 and post['data']['upvote_ratio'] > 0.8:
      return True
    else:
      return False
  
  def not_already_posted(self,post):
    name = post['data']['name']
    post = Post.get_or_none(reddit_id=name)
    return post is None

  def calc_rating(self, upvotes, upvote_ratio):
    ups = 100000 if upvotes > 100000 else upvotes
    ups *= upvote_ratio
    return round(self.convert_to_smaller_range(ups), 2)

  def convert_to_smaller_range(self, num):
    oldMax = 100000
    oldMin = 10000
    newMax = 10
    newMin = 6
    oldValue = num

    oldRange = (oldMax - oldMin)  
    newRange = (newMax - newMin)  
    newValue = (((oldValue - oldMin) * newRange) / oldRange) + newMin
    return newValue


  def save_top_and_return_post(self, posts):
    for post in posts:
      if self.is_quality_post(post) and self.not_already_posted(post):
        urllib.request.urlretrieve(post['data']['url_overridden_by_dest'], self.subreddit+".jpg")
        print("saved image from reddit")
        saved_post = self.save_post(post)
        return saved_post

  def save_post(self, post):
    data = post['data']
    r_id = data['name']
    url = data['url_overridden_by_dest']
    r = self.calc_rating(data['ups'], data['upvote_ratio'])

    saved_post = Post.create(reddit_id=r_id, image_url=url, subreddit=self.subreddit, rating=r)
    return saved_post

  def delete_post(self, post):
    post.delete_instance()

  def delete_saved_image(self):
    os.remove(self.subreddit+".jpg")
