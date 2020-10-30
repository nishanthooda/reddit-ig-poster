#!/usr/bin/python3
from db.create_database import Post
from peewee import *
from pull_reddit import PullReddit
from insta_poster import InstaBot
from db.create_database import Post
from dotenv import load_dotenv
import os

load_dotenv()

# HOLUP
red_holup = PullReddit("holup")
posts_holup = red_holup.get_top_historic_data("week")
new_post_holup = red_holup.save_top_and_return_post(posts_holup)
i_holup = InstaBot(os.getenv("HOLUP_USERNAME"), os.getenv("HOLUP_PASSWORD"), new_post_holup.subreddit, new_post_holup.rating)
if not i_holup.successfully_made_post():
  red_holup.delete_post(new_post_holup)
red_holup.delete_saved_image()

# MADLADS
red_madlads = PullReddit("madlads")
posts_madlads = red_madlads.get_top_historic_data("week")
new_post_madlads = red_madlads.save_top_and_return_post(posts_madlads)
i_madlads = InstaBot(os.getenv("MADLADS_USERNAME"), os.getenv("MADLADS_PASSWORD"), new_post_madlads.subreddit, new_post_madlads.rating)
if not i_madlads.successfully_made_post():
  red_madlads.delete_post(new_post_madlads)
red_madlads.delete_saved_image()