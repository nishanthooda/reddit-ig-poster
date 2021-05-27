# MemeBot

Gets memes from reddit to post them on an instagram meme account. 

# How it works

1. Python script uses Reddit API to fetch the top post from specified subreddit and downloads the associated image.
2. Selenium then opens Instagram on chrome, logs into the account, and then posts the image with specified caption.
3. A "rating" is generated in the caption based on how many upvotes the post had on reddit.

SQLlite is used to track past downloaded posts to ensure same meme isn't posted twice. 

# Demo

Selenium was having issues with a screen recorder running. So here's a shaky iPhone video instead 😃

https://user-images.githubusercontent.com/26640020/119899189-a89d1b00-bef7-11eb-951e-022ae63f7461.MOV

# Next Steps
- Deploy to an Lambda instance and set it to run automatically twice a day. 
