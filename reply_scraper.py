"""
Reply script
"""
#!/usr/bin/env python
#
# Sweary Robot by Keith Baker
#
from datetime import datetime, timedelta
import random
import tweepy
from SwearyRobot import swear, twitterName
from sweary_creds import apiKey, apiSecret, accessToken, accessSecret

#
# set auth
auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessSecret)
api = tweepy.API(auth)

#
# sweary sentences
speaktome = ("HOW DARE YOU! %s, you're a %s %s", "Never speak to me like that, %s you %s %s!!", 
             "Fuck off %s #%s%s", "It's people like you, %s who make %s %s!", "STFU %s, Your %s is %s!!", 
             "%s FUCK YOUR %s %s!!", "Yeah, %s Stick a %s up your %s!!", 
             "%s's face is %s multiplied by %s", "Yeah, %s, whatever. #%s%s", 
             "%s, %s's like you should shut their %s", "#%s%s%s", 
             "Well, %s All I heard was you calling yourself %s %s.", "Yeah, %s your %s is amazing. #%s", 
             "This is %s a perfect example of %s %s.", 
             "So, %s. Bleeding from the %s are we? Explains the %s.", 
             "%s I hope you die of %s %s", "%s, you're a %s %s!", 
             "ME. %s?!?! %s you, you %s!!", "Shut up %s! I've %s'd bigger %ss than you!!", 
             "Hey, %s you %s your mum with that %s?", "%s? More like %s%s.", 
             "The world needs more people like %s, the fucking %s%s!!", "No, %s. Just %sing no you %s.", 
             "So, %s. Think your %s is clever do you? %s off! #%s", 
             "Fuck %s. Fuck their %s with a %s!", "So %s opened their stupid %sy mouth. Fuckin' %s.")
#
# check last 3 minutes

timestamp = datetime.now() - timedelta(minutes=3)
results = api.search(q="@" + twitterName)
#
# if there's anything, lay into the bastards!
for result in results:
    if "RT" not in result.text and result.created_at > timestamp:
        twerp = "@%s %s" % (result.user.screen_name, random.choice(speaktome) % (
            result.user.name, random.choice(swear), random.choice(swear)))
        api.update_status(twerp)
