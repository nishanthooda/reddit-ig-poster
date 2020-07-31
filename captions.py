class Captions:
  def __init__(self):
    return
  
  def generate_caption(self,subreddit,rating):
    rating = str(rating)
    if subreddit == "holup":
      return "Holup Rating: " + rating + """/10
Tag a friend to share the laugh!
.
.
.
.
.
#holdup #meme #funny #holup #memes #dankmemes #bestmemes #instamemes #funny #funnymemes #offensivememes #nichememes #memepage #funniestmemes #dank #memesdaily #jokes #memesrlife #memestar #memesquad #humor #lmao #igmemes #lol #memeaccount #relatablememes #funnyposts #sillymemes #nichememe #memetime"""
    elif subreddit == "madlads":
      return "Madlad Rating: " + rating + """/10
Tag a friend to share the laugh!
.
.
.
.
.
#madlad #meme #funny #madlads #memes #dankmemes #bestmemes #instamemes #funny #funnymemes #offensivememes #nichememes #memepage #funniestmemes #dank #memesdaily #jokes #memesrlife #memestar #memesquad #humor #lmao #igmemes #lol #memeaccount #relatablememes #funnyposts #sillymemes #nichememe #memetime"""

