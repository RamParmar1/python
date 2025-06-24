#Instagram automation using python
#pip install instabot
from instabot import Bot
bot = Bot()
bot.login(username = "",password = "")

bot.follow('') #automatic follow any user

bot.upload_photo("",caption = "") #in path change \ to this /

bot.unfollow('') #automatic unfollow any user

bot.send_message("",["",""]) #multiple message send first message then square bracket user but it will send in the group

followers = bot.get_user_followers("") #user-id
for follower in followers:
    print(bot.get_user_info(follower)) # we also can do the filter in for loop for if large number of follower list

following = bot.get_user_following("") #user-id
for Following in following:
    print(bot.get_user_info(following)) #we also can do the filtering if want otherwise get result of large number of data list

#There are also many other function of do the task in instagram from python prompt
#but here most off functionlity's are there if you use pycharm editor then you can find many manual functionalitites.
#only you do in this program is give information in single-quote and double-quote.
