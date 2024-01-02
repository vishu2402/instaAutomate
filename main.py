from instabot import Bot
bot=Bot()
bot.login(username="___v.i.s.h.u",password="Classy_2402")
bot.follow('shreyash_iyyer')
bot.upload_photo("file:///C:/Users/kumar/Downloads/Top-100-Crypto-Memes-of-2022-59-crypto-vs-bank-account.webp", caption="Crypto Memes")
bot.unfollow('shreyash_iyyer')
bot.send_message("I love crypto", ["nitin_yadav"])
followers=bot.get_user_followers("___v.i.s.h.u")
for follower in followers:
    print(bot.get_user_info(follower))
following=bot.get_user_following("___v.i.s.h.u")
for Following in following:
    print(bot.get_user_info(Following))
