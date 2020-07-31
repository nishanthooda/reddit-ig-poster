from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from pyautogui import press, write, hotkey, KEYBOARD_KEYS
from captions import Captions
from random import randrange
import random

class InstaBot:
  def __init__(self, username, pw, subreddit, rating):
    self.username = username
    self.pw = pw
    self.subreddit = subreddit
    self.post_rating = rating

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/83.0.4103.116 Mobile/15E148 Safari/604.1"')
    self.driver = webdriver.Chrome(options=chrome_options)

  def login(self):
    self.driver.get("https://instagram.com")
    self.sleep_random()
    #Log in button
    self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[2]/button").click()
    self.sleep_random()
    self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
    self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.pw)
    self.driver.find_element_by_xpath('//button[@type="submit"]').click()
    self.sleep_random()
  
  def close_popups(self):
    #Not Now Button
    self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/button").click()
    self.sleep_random()
    
    #Cancel on adding to home screen
    self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    self.sleep_random()
  
  def post(self):
    #Post button
    self.driver.find_element_by_xpath("/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]").click()
    self.sleep_random()
    write('/')
    self.sleep_random()
    write('Users/nishant/git/reddit-ig-poster', interval=0.05)
    press('return')
    self.sleep_random()
    write(self.subreddit, interval=0.1)
    press('return')
    self.sleep_random()

    # Scroll to bottom
    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    self.sleep_random()

    # Resize image Button
    self.driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div[2]/div/div/div/button[1]").click()
    self.sleep_random()

    # Scroll to top
    self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    self.sleep_random()
    
    # Next Button
    self.driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button").click()
    self.sleep_random()
    c = Captions()
    caption = c.generate_caption(self.subreddit, self.post_rating)
    # Type caption
    self.driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea").send_keys(caption)
    self.sleep_random()
    # Post 
    self.driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button").click()
    sleep(5)

  def successfully_made_post(self):
    try:
      self.login()
      self.close_popups()
      self.post()
      self.driver.close()
    except:
      print("failed to post")
      self.driver.close()
      return False
    else:
      print("sucessfully posted")
      return True

  def sleep_random(self):
    num = 1+random.randint(1,3)
    sleep(num)
