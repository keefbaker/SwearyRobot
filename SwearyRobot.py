#!/usr/bin/env python
#
# Sweary Robot by Keith Baker
#
import tweepy
import random
from holly import celebgrab
from sweary_creds import apiKey, apiSecret, accessToken, accessSecret
#
# set auth
auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessSecret)
import time
api = tweepy.API(auth)

#
# Pull followers through
ids = [user.screen_name for user in tweepy.Cursor(api.followers, screen_name="SwearyRobot").items()]

#
# Pull hashtags through
trends1 = api.trends_place(1)
hashtags = [x['name'] for x in trends1[0]['trends'] if x['name'].startswith('#')]

#
# It's combination list time!
# 
superlative = [ "Super", "Ultra", "Mega", "Ultra", "Weak", "Weepy", "Mad", "Rage", "Sad", "Farty", "Disgust-o-", "Bilious", "Pre-raphaelite-", "Vomito", "Arthurian-", "Bad", "cavernous", "Good", "Insdious", "Rupert-Murdochian-", "Cry", "Foxnews", "Stilted-", "Impossa", "Bleeding ", "Nostril", "Diahorretic", "Enochian ", "Cockripping ", "Sharp", "Evil", "Disturbing ", "Jerkwad ", "Screwy ", "Arseweeping-", "Scagged-up ", "Stink", "Gunked-up ", "Fisted ", "Smeared ", "Disappointing-", "Pus-filled ", "Botty", "Dingle", "Pissy", "Rancid ", "Rot", "Cacky", "Skank", "Funsize ", "Baby", "Ming", "Dodgy", "Fuck", "Skate", "Dirty", "Death", "Murder", "Frothing wrath", "Porn", "Micro", "Internet", "Massive", "Crotch", "Daily Mail ", "King", "Queen", "Princess", "Lantern-jawed-", "Crack", "Smeg", "Shitty", "Rat", "Lamplicking", "Incontinent ", "Trump", "Waste", "Gun-toting-", "Poo", "Milky", "Slime", "Colonic-", "Classically Greek ", "French rennaissance "]
swear = [ "fuck", "cunt", "arse", "bum", "shit", "motherfucker", "piss", "wank", "vomit", "penis", "twat", "cock", "dumb", "fucknut", "cuntface", "dribble", "wipe", "chunder", "bastard", "mugfucker", "assclown", "bitch", "boner", "clitoris", "chode", "dickhead", "cuntrag", "dipshit", "douche", "nutsack", "pecker", "prick", "queef", "rimjob", "scrote", "shitbag", "skullfuck", "turd", "twatlips", "tit", "fart", "flaps", "jamrag", "bellend", "helmet", "dangler", "cocksnot", "jizz", "goatse", "paedo", "axe-wound", "anus", "brownhole", "dogfuck", "turd", "bottysausage", "pinwilly", "slurry", "asshole", "cackspider", "taint", "barse", "bollocks", "jerk", "residue", "scrotum", "fist", "puke", "crybaby", "pustule", "mom", "vagina", "testes", "marketing bastard", "telemarketer", "armpit hair", "sweaty ballsacks", "adobe FUCKING ACROBAT", "dogmuck" "David Cameron", "porridge", "filth", "scum", "slag", "stain", "drip", "widge", "pigeon", "bag", "hole", "boobs", "twerp", "cheeks", "fanny", "ejaculate", "weasel", "spank", "vibrator", "corpse", "bowels" ]
preposition = [ "I mean %s,  right?", "Just %s!!", "There's %s.", "And there it is... %s.", "For the love of %s.", "For %s's sake!", "I'm raging about %s.", "It... %s just makes me sad.", "You're such a %s!", "This %s just isn't worth my time.", "I know I'm a bot, but %s, right?", "I can't take any more of this %s.", "I'm actually really %s pleased!", "I just ate some %s. It tasted awful!", "This can %s off!", "%s!" "Life would be better without %s, don't you think?", "This is a new design of %s, let me tell you!", "I need some %s for my garage, has anyone got some?", "Your face is a %s!", "Your mum's %s makes me sick.", "Stick %s up your massive arse!", "New %s, please.", "I could do with a %s.", "What this country needs is a new %s.", "I'm not arsed about your your %s, so shut your fucking gob.", "If only the %s was real..", "There's some %s on telly tonight.", "Instagrammed my %s. Not many likes. Feeling sad.", "Amazon have free %s. I paid loads for mine. ", "I am president %s. Fear me!", "20 times I said. %s yourself!" ]
stuff = [ "tea", "toilet", "post office", "work canteen", "fish fingers", "Fenton pub", "salad bowl", "lemon juice", "helicopter cockpit", "DFS sale", "prison shower", "bolognese", "chistmas cake", "garden", "nude", "nearby branch of Tesco", "city of Whiterun", "dog's mouth", "spleen", "hotel towel", "cavernous arse of Alexander the Great", "martian rover", "photocopier outlet", "boot cupboard", "sellotape", "dogs mouth", "queen's ladygarden", "french mustard", "rotting turkey", "butthole of Santa", "dark one's testes", "nuclear waste barrel", "only copy of Half life 3", "last open Woolworths"]
dang = [ "Enough of", "No more", "Had my fill of", "Please stop the", "Less of the", "So much for" ]
dong = [ "So I said,", "Well he thought,", "I don't want", "He said to me,", "I never wanted to hear", "I asked for oil, I didn't say,", "Philosophy:" ]
celebline = [ "I wish %s would %s %s!", "%s has %s'd in the %s. Disgraceful!", "I know %s is famous but %s a %s!", "%s, a classic %s %s", "Woo! %s #%s%s" ]
#
# Time to construct the tweet
#
if random.randrange(20) > 12:
	tweet = random.choice(superlative) + random.choice(swear) + "! " + random.choice(preposition) % random.choice(swear) + " #" + random.choice(superlative) + random.choice(swear)
elif random.randrange(20) < 2:
	tweet = "@%s OI %s! Why don't you %s in the %s, you fucking %s!!" % (random.choice(ids),random.choice(superlative) + random.choice(swear), random.choice(swear), random.choice(stuff), random.choice(swear))
elif random.randrange(20) < 8:
	tweet = "%s %s in the %s. %s. #%s" % (random.choice(dang), random.choice(swear), random.choice(stuff), random.choice(preposition) % random.choice(swear), random.choice(swear))
elif random.randrange(20) < 5:
	tweet = "No idea what this %s is about. %s %s" % (random.choice(swear), random.choice(preposition) % random.choice(swear), random.choice(hashtags))
elif random.randrange(20) < 9:
	tweet = random.choice(celebline) % (celebgrab(), random.choice(swear),random.choice(swear))
else:
	masstrack = random.choice(superlative) + random.choice(swear)
	supermasstrack = random.choice(preposition) % masstrack
	tweet = "%s %s But screw this %s." % (random.choice(dong),supermasstrack,random.choice(swear))

#
# And finally post the mother
#
if __name__ == "__main__":
	if random.randrange(20) < 20:
		api.update_status(tweet)
